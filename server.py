import sys
# Add the current directory to sys.path to resolve relative imports in container environment
sys.path.append(".")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tools.search import web_search

# Initializes the FastAPI application instance.
app = FastAPI()  # must come BEFORE decorators

# Adds CORS middleware to allow cross-origin requests from any source,
# enabling frontend compatibility during development or deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/web_search")
# Defines the API endpoint for web search requests.
# It accepts a JSON payload (dictionary) containing search parameters.
async def web_search_endpoint(tool_input: dict):
    # Calls the core business logic function to perform and structure the web search.
    return await web_search(tool_input)