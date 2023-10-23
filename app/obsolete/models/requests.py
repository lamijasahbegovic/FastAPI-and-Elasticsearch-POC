from typing import Optional
from pydantic import BaseModel, Field


class MovementRequestBody(BaseModel):
    name: str = Field(...)
    from_year: int = Field(...)
    to_year: int = Field(...)
    description: str | None = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Baroque",
                "from_year": "1700",
                "to_year": "1800",
                "description": "...",
            }
        }


class ArtistRequestBody(BaseModel):
    name: str = Field(...)

    class Config:
        json_schema_extra = {"example": {"name": "Monet"}}
