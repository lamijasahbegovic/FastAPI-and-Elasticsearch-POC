from typing import Optional
from pydantic import BaseModel, Field


class MovementModel(BaseModel):
    name: str = Field(...)
    from_year: int = Field(...)
    to_year: int = Field(...)
    description: Optional[str] = Field(default=None)
    characteristics: Optional[list[str]] = Field(default=None)
    key_figures: Optional[list[str]] = Field(default=None)
    major_works: Optional[list[str]] = Field(default=None)
    influences: Optional[list[str]] = Field(default=None)
    tags: Optional[list[str]] = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Impressionism",
                "from_year": "1860",
                "to_year": "1910",
                "description": "A 19th-century art movement...",
                "characteristics": ["Brushstroke", "Light"],
                "key_figures": ["Claude Monet", "Pierre-Auguste Renoir"],
                "major_works": ["Water Lilies", "Starry Night"],
                "influences": ["Realism", "Japanese art"],
                "tags": ["Post-Impressionism", "French art"],
            }
        }


mapping = {
    "properties": {
        "name": {
            "type": "text",
        },
        "from_year": {"type": "integer"},
        "to_year": {"type": "integer"},
        "description": {
            "type": "text",
        },
        "characteristics": {"type": "keyword"},
        "key_figures": {"type": "keyword"},
        "major_works": {"type": "keyword"},
        "influences": {"type": "keyword"},
        "tags": {"type": "keyword"},
    }
}
