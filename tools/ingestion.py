import tempfile
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from db.qdrant import vector_store

def ingest_document(
        file_bytes: bytes,
        filename: str,
):

    if not filename.lower().endswith('.pdf'):
        raise ValueError("Only PDF files are supported.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(file_bytes)
        temp_filepath = temp_file.name

    try:
        loader = PyPDFLoader(temp_filepath)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # chunk size (characters)
            chunk_overlap=200,  # chunk overlap (characters)
            add_start_index=True,  # track index in original document
        )

        all_splits = text_splitter.split_documents(docs)
        document_ids = vector_store.add_documents(all_splits)
        return document_ids
    
    except Exception as e:
        raise e
    
    finally:
        os.remove(temp_filepath)