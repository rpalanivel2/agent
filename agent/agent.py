from langchain.agents.structured_output import ToolStrategy
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware


from models.classmodels import Context, ResponseFormat

from config.model import default_model
from tools.tools import get_location, get_weather, retrieve_context 
from prompts.prompts import SYSTEM_PROMPT
from config.config import checkpointer
from middleware.middleware import select_model


agent = create_agent(
    model=default_model,
    tools=[get_location, get_weather, retrieve_context],
    system_prompt=SYSTEM_PROMPT,
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer,
    middleware=[
        select_model,
        SummarizationMiddleware(
            model=default_model,
            trigger=("tokens", 4000),
            keep=("messages", 20),
        )

    ]
)

