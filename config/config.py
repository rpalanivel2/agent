import os
from dotenv import load_dotenv
import langsmith as ls
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

# Memory-based checkpointer for storing intermediate states
checkpointer = InMemorySaver()

TRACE_KEY = os.getenv('TRACE_KEY')

# Tracing client configuration
client = ls.Client(
    api_key=TRACE_KEY,  # This can be retrieved from a secrets manager
    api_url="https://api.smith.langchain.com",  # Update appropriately for self-hosted installations or the EU region
)