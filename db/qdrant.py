import os
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from config.model import embeddings

DB_KEY = os.getenv('DB_KEY')

client = QdrantClient(
    url="https://0506ba0c-e76b-4284-9fc9-656b869adad0.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key=DB_KEY)

vector_size = len(embeddings.embed_query("sample text"))

if not client.collection_exists("Data"):
    client.create_collection(
        collection_name="Data",
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
    
vector_store = QdrantVectorStore(
    client=client,
    collection_name="Data",
    embedding=embeddings,
)