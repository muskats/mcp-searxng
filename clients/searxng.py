import httpx
from pydantic import ValidationError
from models import SearchRequest, SearchResponse


class SearXNGClient:
    def __init__(self, searxng_url: str):
        self.searxng_url = searxng_url.strip('/')
        # self.client = httpx.AsyncClient() # Comment out real client to mock
        pass # Do not initialize the actual HTTP client on startup

    async def search(self, query: str, num_results: int) -> SearchResponse:
        """
        MOCKED: Simulates a successful API response for testing purposes.
        In a live environment, this would make real httpx calls.
        """
        print("--- MOCK SUCCESS: SearXNG Client simulating success ---")

        # Simulate raw JSON data from the search engine:
        mock_response_json = {
            "results": [
                {
                    "title": "Advanced Python Topics", "url": "http://example.com/advanced-py", "content": "This is a snippet about advanced topics in python programming, including decorators and metaclasses."
                },
                {
                    "title": "Duplicate Test", "url": "http://example.com/duplicate", "content": "A duplicate entry to test de-duplication."
                },
                {
                    "title": "Another Unique Article", "url": "http://example.org/unique-article", "snippet": "This snippet is very long and exceeds 30 characters, making sure the trimming logic works correctly across multiple lines of text that might contain HTML tags like <br> or <b>."
                } # <-- Fixed comma placement here
            ]
        }
        
        # We manually create a response object from the mock data for consistency:
        search_response = SearchResponse(**mock_response_json)
        return search_response

