"""
Step 6: Terminal Chat Interface
Loops over user input, prints retrieved chunks (bonus challenge), and shows answers.
"""
from pipeline import run_rag_pipeline

def main():
    print("=" * 60)
    print("        Naive RAG — Chat With Documents App        ")
    print("  Type your question below. Type 'exit' or 'q' to quit.")
    print("=" * 60)

    while True:
        try:
            query = input("\nUser: ").strip()
            if not query:
                continue
            if query.lower() in ["exit", "quit", "q"]:
                print("Exiting chat. Goodbye!")
                break

            result = run_rag_pipeline(query)

            # Bonus Challenge: Print retrieved chunks so the user sees source attribution
            print("\n[Retrieved Chunks Used as Context]:")
            if not result["retrieved_chunks"]:
                print("  (None - No chunk met the relevance distance threshold)")
            else:
                for idx, chunk in enumerate(result["retrieved_chunks"], 1):
                    snippet = chunk['text'].replace('\n', ' ')[:120]
                    print(f"  [{idx}] {chunk['chunk_id']} (Distance: {chunk['distance']:.4f})")
                    print(f"      \"{snippet}...\"")

            print(f"\nAssistant:\n{result['answer']}")

        except KeyboardInterrupt:
            print("\nChat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n[Error]: {e}")

if __name__ == "__main__":
    main()