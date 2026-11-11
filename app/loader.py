import config
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

# Read pdf files
def load_documents(path: str = None):

    if path is None:
        path = config.PATH_DATA_FILE

    pdf_loader = DirectoryLoader(
        path=path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )

    documents = pdf_loader.load()

    return documents