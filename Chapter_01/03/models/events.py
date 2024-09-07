from beanie import Document
from typing import Optional, List
from pydantic import BaseModel

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI book launch",
                "image": "https://image",
                "description": "We will be discussing the contents of the FastAPI book in the event",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "google meet"
            }
        }
    
    class Settings:
        name = "events"

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI book launch",
                "image": "https://images",
                "description": "We will be discussing the contents of the fastapi",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "google meet"
            }
        }