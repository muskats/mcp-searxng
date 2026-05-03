import re
from typing import List
from ..clients.searxng import SearXNGClient
from ..models import SearchRequest, SearchResponse

class SearchService:
    def __init__(self, client: SearXNGClient):
        self.client = client

    @staticmethod
    def _strip_html(text: str) -> str:
        """Removes basic HTML tags from a string."""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    async def search(self, request: SearchRequest) -> SearchResponse:
        """
        Performs the core business logic: calling raw HTTP service, 
        normalizing data, filtering results, and handling errors safely.
        Returns a structured SearchResponse object.
        """
        try:
            # 1. Call the raw client to get JSON response
            raw_response = await self.client.search(request.query, request.num_results)
            
            normalized_results: List[dict] = []
            seen_urls: set[str] = set()

            for item in raw_response.results:
                # 2. Deduplication Check
                if item['url'] in seen_urls:
                    continue
                seen_urls.add(item['url'])

                # 3. Data Normalization and Cleaning
                title = self._strip_html(item.get('title', '')).strip()
                url = item.get('url', '').strip()
                snippet_raw = item.get('content', '') # Using 'content' as per instructions
                
                # Strip HTML and trim snippet to max 300 chars
                snippet_clean = self._strip_html(snippet_raw).strip()[:300]
                
                if not title or not url: 
                    continue # Skip results missing critical data

                normalized_results.append({
                    'title': title,
                    'url': url,
                    'snippet': snippet_clean if snippet_clean else '' # Use empty string, never null
                })
            
            return SearchResponse(results=normalized_results)
        except ValueError as e:
            # CATCH 1: Specific error from client (e.g., JSON failure, connection failure).
            # This means the API was called but failed to provide data.
            print(f"[ERROR] Handled search failure gracefully: {e}")
            return SearchResponse(results=[]) # CRITICAL: Return empty list on known error
        except Exception as e:
            # CATCH 2: All other unexpected errors (network, service crash).
            print(f"[FATAL] An unhandled system error occurred in the search service: {e}")
            return SearchResponse(results=[]) # CRITICAL: Return empty list on fatal error



        except ValueError as e:
            # CATCH 1: Specific error from client (e.g., JSON failure, connection failure).
            # This means the API was called but failed to provide data.
            print(f"[ERROR] Handled search failure gracefully: {e}")
            return SearchResponse(results=[]) # CRITICAL: Return empty list on known error
        except Exception as e:
            # CATCH 2: All other unexpected errors (network, service crash).
            print(f"[FATAL] An unhandled system error occurred in the search service: {e}")
            return SearchResponse(results=[]) # CRITICAL: Return empty list on fatal error
