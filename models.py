# This file defines Pydantic models for the search application.
# These models ensure type safety and data validation throughout the application,
# particularly in API endpoints and internal logic.

from pydantic import BaseModel, Field
from typing import List # Added for better compatibility if used elsewhere, although not strictly needed by Pydantic V2 style here.


class SearchRequest(BaseModel):
    """
    Represents a search request with query and number of results.
    
    Attributes:
        query (str): The search query string.
        num_results (int): The number of results to return. Default is 5,
            with a minimum of 1 and maximum of 10.
    """
    query: str
    num_results: int = Field(default=5, ge=1, le=10)  # Limiting to a reasonable range


class SearchResult(BaseModel):
    """
    Represents a single search result item.
    
    Attributes:
        title (str): The title of the search result.
        url (str): The URL of the search result.
        snippet (str): A brief description or snippet of the result.
    """
    title: str
    url: str
    snippet: str


class SearchResponse(BaseModel):
    """
    Represents the response containing a list of search results.
    
    Attributes:
        results (List[dict]): A list of dictionaries, where each dictionary
                               represents a search result item with title, url, and snippet.
    """
    # We use List[dict] here because the data comes from various sources/clients
    # and we need flexible structure for the response payload.
    results: list[dict]
