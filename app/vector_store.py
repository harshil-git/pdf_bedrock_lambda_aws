from chromadb import Client
from chromadb.config import Settings
from app.embedder import embed_text

def get_vector_store():
    return Client(Settings(
        persist_directory="chroma_store",
        anonymized_telemetry=False
    ))

def get_or_create_collection(client, name="pdf_paragraphs"):
    if name in [c.name for c in client.list_collections()]:
        return client.get_collection(name)
    else:
        return client.create_collection(
            name=name,
            embedding_function=lambda texts: [embed_text(text) for text in texts]
        )
