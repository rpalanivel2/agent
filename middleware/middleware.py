from typing import Callable

from langchain.agents.middleware import SummarizationMiddleware, wrap_model_call, ModelRequest, ModelResponse, dynamic_prompt

from config.model import basic_model, default_model
from prompts.prompts import SYSTEM_PROMPT

chat_history_summarizer = SummarizationMiddleware(
    model=default_model,
    trigger=("tokens", 4000),
    keep=("messages", 20),
)

@wrap_model_call
def select_model(request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
    """Select Model Dynamically based on Context"""
    model_name = request.runtime.context.model_name

    if model_name == "gpt-4.1-mini":
        model = default_model
    else:
        model = basic_model

    return handler(request.override(model=model))

@dynamic_prompt
def dynamic_system_prompt(request: ModelRequest) -> str:
    """Generate system prompt based on user name"""
    user_name = request.runtime.context.user_name

    if user_name == "A":
        return f"{SYSTEM_PROMPT} Provide your responses in a sarcastic and funny tone."
    elif user_name == "B":
        return f"{SYSTEM_PROMPT} Also add a small joke relevant to the user query"
    
    return SYSTEM_PROMPT

