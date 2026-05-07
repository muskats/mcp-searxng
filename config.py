from pydantic_settings import BaseSettings

# Defines the settings class, inheriting from BaseSettings for environment variable loading. 
class Settings(BaseSettings):
    # The base URL for the SearXNG instance. This defaults to a local development setup.
    searxng_url: str = "http://localhost:8080"  # Default SearXNG URL

    class Config:
        # Specifies the file name where environment variables are loaded from (e.g., .env).
        env_file = ".env"
        # Defines the encoding used when reading the specified environment file.
        env_file_encoding = "utf-8"

# Initializes the settings object, loading values from the configured sources.
settings = Settings()
