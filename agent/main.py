from agent.agent import agent
from models.classmodels import Context

from config.config import client
import langsmith as ls

trace_client = client
config = {"configurable": {"thread_id": "1"}}

def call_agent(user_message, userId, userName):
    with ls.tracing_context(client=trace_client, project_name="AI-Agent", enabled=True):
        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_message}]},
            config=config,
            context=Context(
                user_id=userId,
                user_name=userName
            )
        )

    return response.get("structured_response", "No structured response returned").response
