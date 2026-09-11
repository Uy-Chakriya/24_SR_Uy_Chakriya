# Homework Reflection

### 1. What Worked Well
The end-to-end Naive RAG pipeline successfully connected the offline indexing flow (ingest, chunk, embed, and store in ChromaDB) with the online query flow (retrieve and generate). Running both `nomic-embed-text` and `llama3.2` locally via Ollama provided fast, cost-free inference with zero external API dependencies. The temperature setting of 0.0 and explicit system prompt grounding prevented hallucinations and successfully answered on-topic queries.

### 2. What Was Harder Than Expected
Calibrating the chunking strategy and the relevance distance threshold was the trickiest part. Setting the chunk size too small severed multi-step instructions across boundaries, while setting it too large diluted semantic similarity. In addition, picking the right cosine distance threshold for the "No good match" guard required empirical testing to ensure off-topic questions were rejected without rejecting valid on-topic questions.

