import config
from app.loader import load_documents
from app.splitter import split_into_chunk
from app.embedding import get_embedding_model ,embed_document


def main():
    documents=load_documents(config.PATH_DATA_FILE)
    chunks=split_into_chunk(documents)
    vectors=embed_document(chunks)

    print(vectors[0][:5])

if __name__=="__main__":
    main()