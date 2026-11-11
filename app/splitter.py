import config
from langchain_text_splitters import CharacterTextSplitter

def split_into_chunk(documents):
    " split document into  chunks"
    splitter= CharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE ,
        chunk_overlap = config.CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    return chunks 