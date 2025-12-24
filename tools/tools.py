from langchain.tools import tool, ToolRuntime

from models.classmodels import Context 
from db.qdrant import vector_store

import requests

# @tool
# def get_location(runtime: ToolRuntime[Context]) -> str:
#     """Gets the user's current location."""
#     match runtime.context.user_name.lower():
#         case "alice":
#             return "San Francisco"
#         case "bob":
#             return "Chicago"
#         case _:
#             return "New York"

@tool
def get_location(user_name: str) -> str:
    """Gets the user's current location."""
    match user_name.lower():
        case "alice":
            return "San Francisco"
        case "bob":
            return "Chicago"
        case _:
            return "New York"

@tool
def get_weather(location: str) -> str:
    """Gets the weather forecast for a given location."""
    url = 'http://api.weatherapi.com/v1/current.json'
    params = {
        'key': '41fc0858127447eda4a184605251312',
        'q': location,
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        climate = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        return f"The current weather in {location} is {climate} with a temperature of {temp_c}°C."
    except requests.RequestException as e:
        return f"Error fetching weather data: {e}"
    

@tool
def retrieve_context(query: str) -> str:
    """Retrieves relevant context to help answer a given query."""
    retrieved_docs = vector_store.similarity_search(query, k=3)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs