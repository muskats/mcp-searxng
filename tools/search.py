# tools/search.py
from services.search_service import SearchService
from clients.searxng import SearXNGClient
from config import settings
from models import SearchRequest, SearchResponse

async def web_search(tool_input: dict):
    request = SearchRequest(**tool_input)
    client = SearXNGClient(settings.searxng_url)  # Ensure settings are correctly imported
    service = SearchService(client)

    results = await service.search(request)
    return {"results": [result.dict() for result in results]}