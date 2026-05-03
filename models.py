from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    query: str
    num_results: int = Field(default=5, ge=1, le=10)  # Limiting to a reasonable range

class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

class SearchResponse(BaseModel):
    results: list[SearchResult]
    