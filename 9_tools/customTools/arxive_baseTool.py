from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain.retrievers import ArxivRetriever

class ArxiveSearchInput(BaseModel):
    query: str = Field(require=True, description="The Query")
    k: int = Field(require=True, description="Total Search result should be returned")
    full_document: bool = Field(False, description="Return  the Full Documents")
    load_all_meta: bool = Field(False, description="Return the Metadat of each Document object")



class ArxiveSearchTool(BaseTool):
    name: str = "ArxiveTool"
    description: str = "Arxive tools basedd on Retriever with Retriever features"
    args_schema: Type[BaseModel]=ArxiveSearchInput

    def _run(self, query: str, k: int, full_document: bool = False, load_all_meta: bool = False):
        retriever = ArxivRetriever(
            top_k_results=k,
            get_full_documents=full_document,
            load_all_available_meta=load_all_meta,
        )
        docs = retriever.invoke(query)
        return docs