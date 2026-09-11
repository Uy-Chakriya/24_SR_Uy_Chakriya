"""
Stage 4 (Online Pipeline):
Embeds the incoming user question and retrieves top matching chunks.
Includes the bonus challenge threshold check.
"""
from typing import List, Dict, Any
from embeddings import embed_query
from vector_store import ChromaVectorStore
from config import TOP_K, DISTANCE_THRESHOLD

def retrieve_context(query: str, top_k: int = TOP_K) -> List[Dict[str, Any]]:
    """
    Takes user query, embeds it, queries ChromaDB, and returns top chunks.
    """
    query_vector = embed_query(query)
    store = ChromaVectorStore()
    hits = store.query(query_vector, top_k=top_k)

    # Bonus Challenge: If closest chunk is not a strong match, return empty
    if hits and hits[0]["distance"] > DISTANCE_THRESHOLD:
        return []

    return hits