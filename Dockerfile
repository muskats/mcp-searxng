# Use the required base image
FROM python:3.11-slim

# Set environment variable for unbuffered output (critical for STDIO communication)
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy dependency files first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining source code
COPY . .

# The entrypoint specifies how the container should run, using 'mcp_searxng' 
# as the module name for server.py (assuming a package structure).
ENTRYPOINT ["/bin/sh", "-c", "python server.py; tail -f /dev/null"]
# Define the command if running without arguments (optional, but good practice)
CMD []