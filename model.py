from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    """nested model class for Todo"""
    id: int
    item: Item


class TodoItem(BaseModel):
    """model for processing the client's request"""
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }


class TodoItems(BaseModel):
    """model for processing the server's response"""
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }