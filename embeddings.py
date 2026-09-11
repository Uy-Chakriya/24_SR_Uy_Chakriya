"""
Stage 3: EMBED
Generates vector representations using the local Ollama nomic-embed-text model.
"""
import ollama
from typing import List
from config import EMBED_MODEL

def embed_texts(texts: List[str]) -> List[List[float]]:
    """
    Embeds multiple text passages sequentially.
    """
    vectors = []
    for text in texts:
        res = ollama.embeddings(model=EMBED_MODEL, prompt=text)
        vectors.append(res["embedding"])
    return vectors

def embed_query(query: str) -> List[float]:
    """
    Embeds a single incoming user question.
    """
    res = ollama.embeddings(model=EMBED_MODEL, prompt=query)
    return res["embedding"]