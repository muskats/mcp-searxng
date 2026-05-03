# Project Goal

The goal of this project is to build a production-grade MCP (Model Context Protocol) server named `mcp-searxng`.

The system must:

- Provide a "web_search" tool to MCP clients (LM Studio)
- Use a SearXNG instance as the search backend
- Be fully free (no paid APIs)
- Be implemented entirely in Python
- Be deployable as a Docker container
- Communicate via STDIO (strict MCP requirement)

Final architecture:

LM Studio → Docker container → Python MCP server → SearXNG HTTP API

The output must always be structured, minimal, and deterministic.

# Architecture Rules

Strict separation of concerns must be enforced:

- server.py
  - MCP entrypoint only
  - tool registration
  - NO business logic

- tools/search.py
  - MCP tool interface
  - input validation
  - calls service layer
  - NO HTTP logic

- services/search_service.py
  - business logic
  - result filtering, normalization
  - error handling

- clients/searxng.py
  - raw HTTP calls only
  - NO transformation logic

Violations of this structure are not allowed.

# MCP Protocol Rules

The MCP server communicates over STDIO.

Critical constraints:

- STDOUT is reserved ONLY for MCP protocol messages
- Logging must NEVER go to STDOUT
- Logging must go to STDERR only

The server must:

- Never crash
- Never emit invalid JSON
- Never print debug logs to STDOUT

If any error occurs:
- Return: { "results": [] }
- Do not raise exceptions to the MCP layer

# Tool Specification

Tool name: web_search

Input:
{
  "query": string,
  "num_results": int (default 5, max 10)
}

Output:
{
  "results": [
    {
      "title": string,
      "url": string,
      "snippet": string
    }
  ]
}

Rules:

- Always validate inputs
- Always return structured output
- Never return raw SearXNG data
- Never include null values
- Limit results to num_results

# Data Normalization Rules

All results must:

- Have non-empty title and url
- Use "content" from SearXNG as "snippet"
- Trim snippet to max 300 characters
- Remove duplicates (by URL)
- Strip HTML tags if present

If data is missing:
- Use empty string, never null

# Docker Requirements

The project must be containerized.

Requirements:

- Base image: python:3.11-slim
- Must run via:
  python -m mcp_searxng.server

- Must support STDIO communication
- Must not buffer output (PYTHONUNBUFFERED=1)

LM Studio will run container using:

docker run -i --rm mcp-searxng

The container must:

- Stay alive
- Accept stdin
- Output MCP responses via stdout

# Verification Rules

Before completing any task, the system must verify:

1. Does the code respect architecture boundaries?
2. Does it break MCP STDIO rules?
3. Does it introduce stdout logging?
4. Does it return consistent schema?
5. Does it handle failure safely?

If any answer is "no", the solution is invalid.

# Suggestion Policy

When making suggestions:

- Prefer minimal, working solutions first
- Avoid overengineering
- Do not introduce frameworks
- Only suggest improvements that align with project goals

Allowed suggestions:

- performance improvements
- reliability improvements
- better error handling
- Docker optimization

Disallowed suggestions:

- switching to Node.js
- adding paid APIs
- adding heavy frameworks
