from pydantic import BaseModel

class ResponseFormat(BaseModel):
    """Class to define response format for the agent."""
    response: str
    location: str | None = None
    temperature_high: str | None = None
    temperature_low: str | None = None
    weather_condition: str | None = None

class Context(BaseModel):
    """Context for tool execution."""
    user_id: str
    user_name: str 