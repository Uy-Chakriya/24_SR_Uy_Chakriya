"""
Step 4 Checklist:
Standalone script to verify the vector store searches correctly before running the chat app.
"""
from embeddings import embed_query
from vector_store import ChromaVectorStore
from config import TOP_K

def main():
    store = ChromaVectorStore()
    print("=" * 60)
    print("        Vector Store Sanity Check (Step 4)        ")
    print("=" * 60)
    
    test_query = input("Enter a test search question: ").strip()
    if not test_query:
        test_query = "How do I configure the VPN for remote work?"

    print(f"\nSearching vector store for: '{test_query}'")
    query_vec = embed_query(test_query)
    results = store.query(query_vec, top_k=TOP_K)

    print(f"\nTop {len(results)} chunks returned:")
    for i, res in enumerate(results, 1):
        print(f"\n[{i}] Chunk: {res['chunk_id']} | Distance: {res['distance']:.4f}")
        print(f"Source: {res['source']}")
        print(f"Content:\n{res['text']}")

if __name__ == "__main__":
    main()