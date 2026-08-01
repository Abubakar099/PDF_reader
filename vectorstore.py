from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def create_vectorstore(text, persist_directory="chroma_db"):
    """
    Text ko chunks mein todta hai, embeddings banata hai,
    aur ChromaDB mein store karta hai.
    """
    # Step 1: Text in  chunks 
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,     # har chunk mein zyada se zyada 1000 characters
        chunk_overlap=200,    # consecutive chunks 200 characters overlap karenge (context na toote isliye)
    )
    chunks = splitter.split_text(text)
    print(f"Text {len(chunks)} chunks mein toota gaya")

    # Step 2: Free embedding model loaded  (dowload for first time )
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # chunks convert into embedding then save in chroma 
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
    )
    print(f"Vectorstore ban gaya aur '{persist_directory}' folder mein save ho gaya")

    return vectorstore


def load_vectorstore(persist_directory="chroma_db"):
    """
    Pehle se bana hua vectorstore wapas load karta hai (dobara embed karne ki zaroorat nahi).
    """
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
    )
    return vectorstore


# Testing ke liye
if __name__ == "__main__":
    from pdf_loader import extract_text_from_pdf

    text = extract_text_from_pdf("Linked List.pdf")
    vectorstore = create_vectorstore(text)

    # Test search 
    query = "yeh document kis baare mein hai?"
    results = vectorstore.similarity_search(query, k=2)

    print("\n--- Top matching chunks ---")
    for i, doc in enumerate(results):
        print(f"\nChunk {i+1}:\n{doc.page_content[:300]}")
