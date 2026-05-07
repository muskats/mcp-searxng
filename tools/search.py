# tools/search.py
# This module orchestrates the search process by combining services and clients.
from services.search_service import SearchService # Imports the service layer logic.
from clients.searxng import SearXNGClient # Imports the specific client implementation.
from config import settings # Accesses global configuration settings (e.g., API URL).
from models import SearchRequest, SearchResponse # Imports necessary data structures.

async def web_search(tool_input: dict): # The main public function called by the FastAPI endpoint.
    # 1. Data Validation/Input Parsing: Creates a validated request object from the raw dictionary input.
    request = SearchRequest(**tool_input) 
    # 2. Client Initialization: Instantiates the low-level API client using configured settings.
    client = SearXNGClient(settings.searxng_url)  # Ensure settings are correctly imported
    # 3. Service Initialization: Passes the client to the service layer, which holds the business logic.
    service = SearchService(client)

    # Executes the search through the service layer and awaits the structured response.
    results = await service.search(request)
    
    # Returns a dictionary containing the results list, matching the expected API output structure.
    return {"results": [result.dict() for result in results]}