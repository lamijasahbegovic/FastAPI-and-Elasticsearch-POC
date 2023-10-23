from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ES_HOST: str = "http://elasticsearch:9200"


settings = Settings()
