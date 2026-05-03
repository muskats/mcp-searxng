import sys
# Add the current directory to sys.path to resolve relative imports in container environment
sys.path.append(".")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tools.search import web_search

app = FastAPI()  # must come BEFORE decorators

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/web_search")
async def web_search_endpoint(tool_input: dict):
    return await web_search(tool_input)