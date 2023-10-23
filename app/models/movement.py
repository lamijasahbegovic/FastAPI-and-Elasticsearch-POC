from typing import Optional
from pydantic import BaseModel, Field


class MovementModel(BaseModel):
    name: str = Field(...)
    from_year: int = Field(...)
    to_year: int = Field(...)
    origin: str = Field(...)
    description: Optional[str]
    characteristics: Optional[list[str]]
    key_figures: Optional[list[str]]
    tags: Optional[list[str]]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Impressionism",
                "from_year": "1860",
                "to_year": "1910",
                "origin": "France",
                "description": "A 19th-century art movement...",
                "characteristics": ["Brushstroke", "Light"],
                "key_figures": ["Claude Monet", "Pierre-Auguste Renoir"],
                "tags": ["Post-Impressionism", "French art"],
            }
        }
