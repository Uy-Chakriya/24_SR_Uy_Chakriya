"""
Stage 2: CHUNK
Splits documents into overlapping chunks using natural character boundaries.
"""
from typing import List, Dict

def recursive_character_split(text: str, chunk_size: int = 800, chunk_overlap: int = 120) -> List[str]:
    """
    Splits text by chunk_size with sliding chunk_overlap.
    Prefers breaking on paragraph breaks or sentence boundaries.
    """
    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunk = text[start:end]

        if end < text_len:
            # Look backwards for a natural break
            boundary = max(chunk.rfind("\n\n"), chunk.rfind("\n"), chunk.rfind(". "))
            if boundary > chunk_size // 2:
                end = start + boundary + (2 if chunk[boundary:boundary+2] in ["\n\n", ". "] else 1)
                chunk = text[start:end]

        chunks.append(chunk.strip())
        if end >= text_len:
            break
        start = end - chunk_overlap

    return [c for c in chunks if c]

def split_documents(documents: List[Dict[str, str]], chunk_size: int = 800, chunk_overlap: int = 120) -> List[Dict[str, str]]:
    """
    Takes loaded documents and converts them into indexed chunks.
    """
    all_chunks = []
    for doc in documents:
        splits = recursive_character_split(doc["text"], chunk_size, chunk_overlap)
        for idx, chunk_text in enumerate(splits):
            all_chunks.append({
                "chunk_id": f"{doc['doc_id']}_chunk_{idx}",
                "text": chunk_text,
                "source": doc["source"]
            })
    return all_chunks