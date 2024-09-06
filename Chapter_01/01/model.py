from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: list[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1"
                    },
                    {
                        "item": "Example schema 2"
                    }
                ]
            }
        }

class Item(BaseModel):
    item: str
    status: str

    class Config:
        json_schema_extra = {
            "Example": {
                "item": "Example 2",
                "status": "Status text"
            }
        }

