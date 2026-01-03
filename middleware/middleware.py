from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from models.classmodels import Context 
from config.model import basic_model, default_model

from typing import Callable

@wrap_model_call
def select_model(request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
    model_name = request.runtime.context.model_name

    if model_name == "gpt-4.1-mini":
        model = default_model
    else:
        model = basic_model

    return handler(request.override(model=model))