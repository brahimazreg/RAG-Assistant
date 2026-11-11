from app.loader import load_documents
from app.splitter import split_into_chunk
import config

def main():
    documents = load_documents(config.PATH_DATA_FILE)
    response= split_into_chunk(documents)

    print(f"Number of chunks: {len(response)}")
    print("=" * 50)

    for i, chunk in enumerate(response[:5]):
        print(f"\n--- Chunk {i} ---")
        print(f"Length: {len(chunk.page_content)}")        
        print(chunk.page_content[:500])  

if __name__ == "__main__":
    main()