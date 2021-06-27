import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from loguru import logger

import sqlite3
from typing import List, Dict, Optional

from backend.database_interaction import create_database_if_not_exist, TodoItem

app = FastAPI()
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
# Now the image is available through http://0.0.0.0:5000/static/puffin-5246026_1920.jpg

db: Optional[sqlite3.Connection] = None

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/api")
async def show_all_todos() -> List[Dict[str, str]]:
    todos = []
    if db:
        for row in db.execute("SELECT id, task FROM todos"):
            todos.append({
                "id": row[0],
                "content": row[1],
            })
    return todos


@app.post("/api/{todo_description}")
async def create_new_todo(todo_description: str):
    # https://fastapi.tiangolo.com/advanced/using-request-directly/
    if todo_description:
        logger.info(f"Attempting to insert new todo: {todo_description}")
        if db:
            db.execute("INSERT INTO todos (task) VALUES (?)", [todo_description])
            db.commit()


# Alternative to above with request body:
@app.post("/api_body")
async def create_new_todo2(request: Request):
    """
    Example with accessing request body.
    Send a request with body {"new_todo": "<todo task description>"}
    """
    # https://fastapi.tiangolo.com/advanced/using-request-directly/
    json_response = await request.json()
    todo_item = json_response.get("new_todo", None)
    if todo_item:
        logger.info(f"Attempting to insert new todo: {todo_item}")
        if db:
            db.execute("INSERT INTO todos (task) VALUES (?)", [todo_item])
            db.commit()


# Alternative to above with model:
@app.post("/api_model")
async def create_new_todo3(item: TodoItem):
    """
    Example with accessing request body.
    Send a request with body {"todo_description": "<todo task description>"}
    """
    # https://fastapi.tiangolo.com/tutorial/body/#import-pydantics-basemodel
    logger.info(f"Received item: {item}")
    if item and item.todo_description:
        logger.info(f"Attempting to insert new todo: {item.todo_description}")
        if db:
            db.execute("INSERT INTO todos (task) VALUES (?)", [item.todo_description])
            db.commit()


@app.delete("/api/{todo_id}")
async def remove_todo(todo_id: int):
    """ Example of using /api/itemid with DELETE request """
    logger.info(f"Attempting to remove todo id: {todo_id}")
    if db:
        db.execute("DELETE FROM todos WHERE id==(?)", [todo_id])
        db.commit()


create_database_if_not_exist()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
