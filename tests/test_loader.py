from app.loader import load_documents
import config

def main():
    documents = load_documents(config.PATH_DATA_FILE)

    print(f"Number of documents: {len(documents)}")
    print("=" * 50)

    first_document = documents[10]

    print("CONTENT:")
    print(first_document.page_content[:500])

    print("=" * 50)

    print("METADATA:")
    print(first_document.metadata)


if __name__ == "__main__":
    main()