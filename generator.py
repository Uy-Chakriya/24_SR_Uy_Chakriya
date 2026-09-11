"""
Stage 5: GENERATE
Constructs a grounded prompt using retrieved chunks and calls local llama3.2.
"""
import ollama
from typing import List, Dict, Any
from config import GEN_MODEL

def generate_answer(query: str, context_chunks: List[Dict[str, Any]]) -> str:
    """
    Concatenates retrieved chunks into context and instructs llama3.2 to answer.
    """
    # Fallback if no context chunks met relevance threshold
    if not context_chunks:
        return "I could not find this in your documents."

    # Naive sequential context concatenation
    context_text = "\n\n---\n\n".join([chunk["text"] for chunk in context_chunks])

    system_prompt = (
        "You are a helpful assistant. Answer the user's question using ONLY the provided context.\n"
        "If the answer cannot be found in the context, state plainly: 'I could not find this in your documents.'\n"
        "Do not make assumptions or use external knowledge."
    )

    user_prompt = (
        f"Context from documents:\n{context_text}\n\n"
        f"Question: {query}\n\n"
        f"Grounded Answer:"
    )

    response = ollama.chat(
        model=GEN_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        options={"temperature": 0.0}
    )

    return response["message"]["content"].strip()