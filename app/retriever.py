import config




def get_retriever(vector_store,k:int=config.TOP_K_RESULT):
    return vector_store.as_retriever(search_kwargs={"k":k})