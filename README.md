# mcp-searxng: Model Context Protocol Web Search Server

## Overview

`mcp-searxng` is an experimental Model Context Protocol (MCP) server. It is designed to provide experimental free web search functionality for large language models (LLMs). It wraps the open SearXNG search engine, transforming its output into a structured format consumable by MCP clients like LM Studio.

The application adheres strictly to the Model Context Protocol (MCP) specification, communicating exclusively via standard input/output (STDIO) to ensure deterministic and minimal interactions with LLM runtimes.

**Goal:** To provide a standardized `web_search` tool that accepts a search query and returns structured results (title, URL, snippet), all while utilizing open-source tools only.

## Prerequisites & Requirements

This project requires several components to function correctly:

1.  **Python Environment:** Python 3.11 or newer.
2.  **Docker:** Docker is required for containerizing the search service.
3.  **SearXNG Instance:** A running SearXNG instance must be accessible. The MCP server expects to communicate with this backend via its HTTP API endpoints. **The SearXNG container/service must be operational before testing.**

### Technical Constraints & Architecture Rules

*   **Communication:** All communication between the LLM client (e.g., LM Studio) and the search service happens over **STDIO**.
*   **Output Integrity:** The MCP server *must only* write valid JSON structures to STDOUT for protocol messages. Logging must be directed exclusively to STDERR.
*   **Security/Reliability**: The system is designed to be resilient, to fail safely, and to handle input validation rigorously. It gracefully returns `{ "results": [] }` upon failure, ensuring the calling MCP layer remains stable.

## Deployment (Docker)

The service is containerized for maximum portability and ease of use.

## Development Context and Implementation Details

This project was developed using a local agent workflow as a test.

### LLM Model

**Gemma**

*   **Generation:** 4
*   **Size**: E4B 

### Hardware

**Lenovo Legion Slim 5 16APH8**
*   **CPU:** AMD Ryzen 7 7840HS w/ Radeon 780M Graphics (3.80 GHz)
*   **RAM:** 16.0 GB RAM
*   **GPU:** NVIDIA GeForce RTX 4070 Laptop GPU (8 GB)

### Development Tools & Ecosystem:

*   **Local LLM Serving:** LM Studio v0.4.12 (used as the local server).
*   **LLM Model:** Gemma 4 (E4B architecture, providing the core intelligence for the agent).
*   **IDE/Editor:** VS Codium.
*   **Agent Framework:** The development process utilized an agent system incorporating Continune and Gemma agents to guide development, enforce architectural boundaries, and validate adherence to the Model Context Protocol (MCP) at every stage.

The structured separation of concerns (Entrypoint → MCP Tool Layer → Service Layer → HTTP Client Layer) was enforced by these tools and the model guidelines provided in `instructions.md`.

This project was developed using a local agent workflow as a test.

**Development Tools & Ecosystem:**
*   **Local LLM Serving:** LM Studio v0.4.12 (used as the local server).
*   **LLM Model:** Gemma 4 (E4B architecture, providing the core intelligence for the agent).
*   **IDE/Editor:** VS Codium.
*   **Agent Framework:** The development process utilized an agent system incorporating Continune and Gemma agents to guide development, enforce architectural boundaries, and validate adherence to the Model Context Protocol (MCP) at every stage.

The structured separation of concerns (Entrypoint → MCP Tool Layer → Service Layer → HTTP Client Layer) was enforced by these tools and the model guidelines provided in `instructions.md`.

## Disclaimer

This project is provided for experimental purposes.

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to:
- correctness of results
- reliability of operation
- fitness for any particular purpose

The author is not responsible for:
- any decisions made based on the output of this software
- inaccuracies or omissions in search results
- failures or downtime of external services (e.g., SearXNG)
- any damages arising from the use of this software

This project depends on third-party tools and services (including but not limited to SearXNG, LM Studio, and LLM models). The behavior and output of these systems are outside the control of the author. All third-party tools are used without endorsement and remain subject to their respective licenses and terms.

Use of this software is entirely at your own risk.

This software is not intended for use in:
- safety-critical systems
- financial decision-making

## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
