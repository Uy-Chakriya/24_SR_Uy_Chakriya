"""
Online Pipeline:
Connects the Retriever and Generator into a unified call:
question in -> grounded answer out.
"""
from typing import Dict, Any
from retriever import retrieve_context
from generator import generate_answer

def run_rag_pipeline(query: str) -> Dict[str, Any]:
    chunks = retrieve_context(query)
    answer = generate_answer(query, chunks)
    return {
        "query": query,
        "retrieved_chunks": chunks,
        "answer": answer
    }