from typing import Dict
from model import Todo, TodoItem, TodoItems
from fastapi import Path, Query, APIRouter, HTTPException, status


router_fn = APIRouter()
request_list = []


@router_fn.post("/todo")
async def add_todo(todo: Todo) -> Dict:
    """function for Route processing, set by Post method

    add the todo to the request_list
    type annotation "Todo" is the custom class defined in model.py for validation of input data type

    Args:
        todo (Dict): a dictionary containing the todo
    """
    request_list.append(todo)
    return {
        "message": "Todo added successfully."
    }


@router_fn.get("/todo", response_model=TodoItems)  # add the response processing model
async def retrieve_todos() -> Dict:
    """function for Route processing, set by Get method

    return the all of todo in request_list
    """
    return {
        "todos": request_list
    }


# {todo_id} is the path parameter
@router_fn.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The Id of the todo to retrieve.")) -> Dict:
    """
    Notes:
         you must provide the path parameter, when you pass the first argument as ...
    """
    for todo in request_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


async def query_route(query: str = Query(None)):
    return query


@router_fn.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> Dict:
    """ function for UPDATE a selected todo"""
    for todo in request_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@router_fn.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> Dict:
    """ function for DELETE a selected todo """
    for index in range(len(request_list)):
        todo = request_list[index]
        if todo.id == todo_id:
            request_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@router_fn.delete("/todo")
async def delete_all_todo() -> Dict:
    """ function for DELETE all todos """
    request_list.clear()
    return {
        "message": "All Todos deleted successfully."
    }

