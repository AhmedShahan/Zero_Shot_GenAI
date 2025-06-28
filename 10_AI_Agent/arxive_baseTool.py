from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from langchain.retrievers import ArxivRetriever

class ArxiveSearchInput(BaseModel):
    query: str = Field(..., description="The query to search for papers")
    k: int = Field(5, description="Number of papers to return")  # Default added
    full_document: bool = Field(False, description="Return full documents")
    load_all_meta: bool = Field(False, description="Load all metadata")

class ArxiveSearchTool(BaseTool):
    name: str = "ArxiveTool"
    description: str = "Search Arxiv using LangChain's ArxivRetriever"
    args_schema: Type[BaseModel] = ArxiveSearchInput

    def _run(self, query: str, k: int = 5, full_document: bool = False, load_all_meta: bool = False):
        retriever = ArxivRetriever(
            top_k_results=k,
            get_full_documents=full_document,
            load_all_available_meta=load_all_meta,
        )
        docs = retriever.invoke(query)
        return "\n".join([d.page_content for d in docs])
