"""
Stage 4 (Store / Retrieve):
Persists chunk vectors to ChromaDB on disk and performs cosine similarity search.
"""
import chromadb
from typing import List, Dict, Any
from config import CHROMA_DIR

class ChromaVectorStore:
    def __init__(self, collection_name: str = "helpdesk_collection"):
        # Persistent mode on disk
        self.client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def add_chunks(self, chunks: List[Dict[str, str]], embeddings: List[List[float]]):
        """
        Upserts chunk vectors and document metadata into the persistent collection.
        """
        ids = [c["chunk_id"] for c in chunks]
        documents = [c["text"] for c in chunks]
        metadatas = [{"source": c["source"]} for c in chunks]

        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )

    def query(self, query_vector: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Retrieves top_k nearest chunks using cosine similarity.
        """
        results = self.collection.query(
            query_embeddings=[query_vector],
            n_results=top_k
        )

        hits = []
        if results["documents"] and len(results["documents"][0]) > 0:
            for i in range(len(results["documents"][0])):
                hits.append({
                    "chunk_id": results["ids"][0][i],
                    "text": results["documents"][0][i],
                    "source": results["metadatas"][0][i]["source"],
                    "distance": results["distances"][0][i] if "distances" in results else 0.0
                })
        return hits