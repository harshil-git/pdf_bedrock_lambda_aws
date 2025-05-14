
from langchain_chroma import Chroma

from app.re_ranker import ranker

from langchain_community.embeddings import HuggingFaceEmbeddings

def query_documents(question: str, persist_directory="./chroma_db", collection_name="pdf_collection", k=5):
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Load existing ChromaDB
    db = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_function,
        persist_directory=persist_directory
    )
    searched_para = db.similarity_search(question)
    #print("Chroma searched para",end="\n\n")
    #print(searched_para)
    
    retrieved_para = [doc.page_content for doc in searched_para]
    #print("retrieved searched para",end="\n\n")
    #print(retrieved_para)

    ranked_para = ranker(question,retrieved_para)
    #print("ranked para",end="\n\n")
    #print(ranked_para)

    return ranked_para
    