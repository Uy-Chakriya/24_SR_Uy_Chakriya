"""
Central configuration for local Naive RAG.
"""

from pathlib import Path


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"               
CHROMA_DIR = BASE_DIR / "chroma_db"           

GENERATION_MODEL = "llama3.2"
EMBEDDING_MODEL = "nomic-embed-text"

CHUNK_SIZE = 800        
CHUNK_OVERLAP = 120     

TOP_K = 3                            

DISTANCE_THRESHOLD = 0.8

EMBED_MODEL = EMBEDDING_MODEL
GEN_MODEL = GENERATION_MODEL
