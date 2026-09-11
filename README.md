# Chat with Documents — Naive RAG Prototype

A local Retrieval-Augmented Generation (RAG) app that answers questions grounded in your own documents. Built as part of the RAG Fundamentals — Week 5 homework.

## Overview

This app implements a full Naive RAG pipeline (ingest → chunk → embed → retrieve → generate) that lets you chat with a folder of your own text documents from the terminal. All models run locally through Ollama, so no data leaves your machine.

## Project Structure

```
.
├── data/                  # Your source documents (.txt / .md)
├── ingestion.py           # Loads raw documents from the data folder
├── chunking.py            # Splits documents into smaller chunks
├── embeddings.py          # Turns chunks into vectors using a local embedding model
├── vector_store.py        # Saves and searches chunk vectors in the vector database
├── retriever.py           # Given a question, finds the most relevant chunks
├── generator.py           # Sends question + chunks to the local LLM, returns an answer
├── pipeline.py            # Connects retriever + generator into one flow
├── main.py                # Runs the terminal chat loop
├── demo_vector_check.py   # Standalone script to sanity-check the vector store
└── README.md
```

## Tech Stack

| Component | Choice |
|---|---|
| Generation model | `llama3.2` (via Ollama) |
| Embedding model | `nomic-embed-text` (via Ollama) |
| Vector database | ChromaDB (persistent mode) |
| Package manager | Poetry |


## Prerequisites

- [Ollama](https://ollama.com) installed and running
- Python 3.10+ and [Poetry](https://python-poetry.org/) installed
- Pull the required models (same command on both platforms, once Ollama is installed):

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

> This is a terminal app. It runs on **Windows** and **macOS** (or Linux). It does **not** run on iOS — Ollama and Poetry are not available on iOS/iPadOS.

## Setup

### Windows

1. Install [Ollama for Windows](https://ollama.com/download/windows) and let it finish setup — it runs in the background automatically.
2. Install Python from [python.org](https://www.python.org/downloads/) (check "Add Python to PATH" during install), then install Poetry:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

   Restart your terminal after installing so `poetry` is on PATH.

3. Clone the repo and install dependencies:

```powershell
git clone <your-repo-url>
cd <your-repo-folder>
poetry install
```

4. Pull the models (Command Prompt or PowerShell):

```powershell
ollama pull llama3.2
ollama pull nomic-embed-text
```

5. Add 3–5 `.txt` or `.md` documents to the `data\` folder.

### macOS

1. Install Ollama:

```bash
brew install ollama
```

   or download it from [ollama.com/download/mac](https://ollama.com/download/mac). Start it if it's not already running:

```bash
ollama serve
```

2. Install Python and Poetry:

```bash
brew install python
curl -sSL https://install.python-poetry.org | python3 -
```

3. Clone the repo and install dependencies:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
poetry install
```

4. Pull the models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

5. Add 3–5 `.txt` or `.md` documents to the `data/` folder.

### Verify the setup (either platform)

Confirm Ollama is running and both models respond before writing/running any RAG code:

```bash
poetry run python <your_test_script>.py
```

## Usage

Commands are identical on Windows and macOS once Poetry and Ollama are set up.

### 1. Build the offline pipeline (ingest, chunk, embed, store)

```bash
poetry run python ingestion.py
```

This loads the documents in `data/`, splits them into chunks, embeds each chunk, and saves the vectors into the vector database.

### 2. Sanity-check the vector store

```bash
poetry run python demo_vector_check.py
```

This embeds a test question, searches the vector database, and prints the top 3 matching chunks so you can confirm retrieval makes sense before chatting.

### 3. Run the chat app

```bash
poetry run python main.py
```

Type your question and press Enter. Type `exit` to quit.

## Chunking Strategy
## Embedding Model & Vector Database

- **Embedding model:** `nomic-embed-text` — _[note dimensionality / why chosen]_
- **Vector database:** ChromaDB (persistent mode) — _[note why chosen, or which alternative you used instead]_

## Testing Each File

Run each module on its own to confirm it works in isolation before running the full app. These assume each file has a small `if __name__ == "__main__":` block for a quick smoke test — add one if it doesn't yet.

```bash
# 1. Ingestion — confirm documents load correctly from data/
poetry run python ingestion.py

# 2. Chunking — confirm documents split into reasonable chunks
poetry run python chunking.py

# 3. Embeddings — confirm a chunk turns into a vector (check the length/shape printed)
poetry run python embeddings.py

# 4. Vector store — confirm chunks save to and can be searched in the database
poetry run python vector_store.py

# 5. Vector store end-to-end check — embed a test question, print top 3 matches
poetry run python demo_vector_check.py

# 6. Retriever — confirm it returns relevant chunks for a sample question
poetry run python retriever.py

# 7. Generator — confirm it builds a prompt and returns an answer from the LLM
poetry run python generator.py

# 8. Pipeline — confirm retriever + generator work together end-to-end
poetry run python pipeline.py

# 9. Full app — run the chat loop
poetry run python main.py
```

