"""
Offline Pipeline:
Executes the full preparation flow once: Ingest -> Chunk -> Embed -> Store.
"""
from config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from ingestion import load_documents
from chunking import split_documents
from embeddings import embed_texts
from vector_store import ChromaVectorStore

def build_index():
    print("--- [Offline Pipeline: Building Index] ---")
    
    # 1. Ingest
    print("[1/4] Loading documents from data/...")
    docs = load_documents(DATA_DIR)
    if not docs:
        print(f"Error: No text documents found in {DATA_DIR}. Please add files.")
        return
    print(f"Loaded {len(docs)} documents.")

    # 2. Chunk
    print("[2/4] Splitting documents into overlapping chunks...")
    chunks = split_documents(docs, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    print(f"Created {len(chunks)} chunks.")

    # 3. Embed
    print("[3/4] Generating vector embeddings using Ollama (nomic-embed-text)...")
    texts = [c["text"] for c in chunks]
    embeddings = embed_texts(texts)

    # 4. Store
    print("[4/4] Storing and indexing vectors into ChromaDB (persistent mode)...")
    store = ChromaVectorStore()
    store.add_chunks(chunks, embeddings)
    print("Indexing completed. Database is saved to chroma_db/\n")

if __name__ == "__main__":
    build_index()