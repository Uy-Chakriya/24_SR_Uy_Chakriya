"""
Stage 1: INGEST
Loads raw text documents from the data/ folder.
"""
from pathlib import Path
from typing import List, Dict

def load_documents(data_dir: Path) -> List[Dict[str, str]]:
    """
    Reads all .txt and .md files in the given directory.
    Returns a list of document dicts with doc_id, text, and source.
    """
    documents = []
    for file_path in data_dir.glob("*.*"):
        if file_path.suffix.lower() in [".txt", ".md"]:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    documents.append({
                        "doc_id": file_path.name,
                        "text": content,
                        "source": str(file_path)
                    })
    return documents