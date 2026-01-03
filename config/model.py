from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

default_model = AzureChatOpenAI(
    model=os.getenv('AZURE_DEPLOYMENT_MODEL'),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_API_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    temperature=0.2
)

basic_model = AzureChatOpenAI(
    model=os.getenv('AZURE_DEPLOYMENT_MODEL2'),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_API_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    temperature=0.2
)

embeddings = AzureOpenAIEmbeddings(
    model=os.getenv('AZURE_EMBEDDING_DEPLOYMENT'),
    api_key=os.getenv('AZURE_EMBEDDING_KEY'),
    api_version=os.getenv('AZURE_EMBEDDING_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
)