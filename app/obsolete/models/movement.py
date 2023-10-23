import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Movement(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    from_year: int = Field(...)
    to_year: int = Field(...)
    description: str | None = Field(default=None)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Baroque",
                "from_year": "1700",
                "to_year": "1800",
                "description": "...",
            }
        }


class MovementUpdate(BaseModel):
    name: Optional[str]
    from_year: Optional[int]
    to_year: Optional[int]
    description: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Baroque",
                "from_year": "1700",
                "to_year": "1800",
                "description": "...",
            }
        }
