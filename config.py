from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    searxng_url: str = "http://localhost:8080"  # Default SearXNG URL

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
