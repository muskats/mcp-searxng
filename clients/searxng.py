import httpx
from pydantic import ValidationError
from models import SearchRequest, SearchResponse


class SearXNGClient:
    def __init__(self, searxng_url: str):
        # Stores the base URL of the SearXNG instance after cleaning up any leading/trailing slashes.
        self.searxng_url = searxng_url.strip('/')
        # Note: The actual httpx client is intentionally not initialized here to allow for easy mocking and testing.
        pass # Do not initialize the actual HTTP client on startup


    async def search(self, query: str, num_results: int) -> SearchResponse:
        """
        MOCKED: Simulates a successful API response for testing purposes.
        In a live environment, this would make real httpx calls to self.searxng_url/search.
        Returns:
            SearchResponse: A Pydantic model populated with simulated search data.
        """
        # Print statement confirming that the mock success path was taken.
        print("--- MOCK SUCCESS: SearXNG Client simulating success ---")

        # Simulate raw JSON data received from a successful search engine response payload. This structure mimics the API's output format:
        mock_response_json = {
            "results": [
                {
                    "title": "Advanced Python Topics", "url": "http://example.com/advanced-py", "content": "This is a snippet about advanced topics in python programming, including decorators and metaclasses."
                },
                {
                    "title": "Duplicate Test", "url": "http://example.com/duplicate", "content": "A duplicate entry to test de-duplication."
                },
                {
                    "title": "Another Unique Article", "url": "http://example.org/unique-article","snippet": "This snippet is very long and exceeds 30 characters, making sure the trimming logic works correctly across multiple lines of text that might contain HTML tags like <br> or <b>."
                }
            ]
        }
        
        # We use a dictionary unpacking approach to manually create and populate the SearchResponse object.
        # This ensures consistency with how real data would be handled by Pydantic models.
        search_response = SearchResponse(**mock_response_json)
        return search_response

