from langchain.agents.structured_output import ToolStrategy
from langchain.agents import create_agent


from models.classmodels import Context, ResponseFormat

from config.model import default_model
from tools.tools import get_location, get_weather, retrieve_context 
from prompts.prompts import SYSTEM_PROMPT
from config.config import checkpointer
from middleware.middleware import select_model, chat_history_summarizer, dynamic_system_prompt
from middleware.errorHandler import tool_error_handler


agent = create_agent(
    model=default_model,
    tools=[get_location, get_weather, retrieve_context],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer,
    middleware=[
        chat_history_summarizer,
        select_model,
        dynamic_system_prompt,
        tool_error_handler
    ]
)

