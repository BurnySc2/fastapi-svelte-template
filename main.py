import asyncio
import json
import time
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

import uvicorn
from fastapi import FastAPI, Request, WebSocket, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from loguru import logger

import sqlite3
from typing import List, Dict, Optional

from starlette.websockets import WebSocketDisconnect

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
def hello_world(response: Response):
    # Set a cookie in the browser
    response.set_cookie("hello", "this is my coookie", expires=24 * 60 * 60)
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


@app.get("/files/bird")
async def show_image():
    """
    Example of making a picture available
    Same image which is available through
    http://0.0.0.0:5000/static/puffin-5246026_1920.jpg
    """
    return FileResponse("backend/static/puffin-5246026_1920.jpg")


##### EXAMPLE WEBSOCKET CHAT
@dataclass
class ChatMessage(DataClassJsonMixin):
    timestamp: float
    author: str
    message: str


class WebsocketChatManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.usernames: Dict[str, WebSocket] = {}
        self.messages_history: List[ChatMessage] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    @staticmethod
    async def send_personal_message(message: str, websocket: WebSocket):
        await websocket.send_text(message)

    @staticmethod
    async def send_personal_json(message: Dict, websocket: WebSocket):
        await websocket.send_text(json.dumps(message))

    async def broadcast_new_message(self, message: ChatMessage):
        self.messages_history.append(message)
        message_to_send = {"newMessage": message.to_dict()}
        for connection in self.active_connections:
            try:
                await self.send_personal_json(message_to_send, connection)
            except RuntimeError:
                await self.disconnect(connection)

    def name_taken(self, name: str):
        return name in self.usernames

    def verify(self, name: str, websocket: WebSocket):
        return name in self.usernames and self.usernames[name] == websocket

    async def connect_username(self, name: str, websocket: WebSocket):
        assert name not in self.usernames
        self.usernames[name] = websocket
        await self.send_personal_json({"connectUser": name}, websocket)
        await self.send_message_history(websocket)

    async def send_message_history(self, websocket: WebSocket):
        await self.send_personal_json({"newMessageHistory": [m.to_dict() for m in self.messages_history]}, websocket)

    async def disconnect_username(self, name: str = None, websocket: WebSocket = None):
        if name is not None:
            assert name in self.usernames
            self.usernames.pop(name)
        else:
            assert websocket
            for username, ws in self.usernames.items():
                if ws == websocket:
                    self.usernames.pop(username)
                    return username


websocket_chat_manager = WebsocketChatManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_chat_manager.connect(websocket)
    try:
        while 1:
            data = await websocket.receive_text()
            data_json = json.loads(data)
            if "message" in data_json:
                # Example message from client on connect
                message = data_json["message"]
                logger.info(f"Message from client was: {message}")
                await websocket_chat_manager.send_personal_json({"message": "Hello from server!"}, websocket)
            elif "tryToConnectUser" in data_json:
                # Client is trying to join chat
                name = data_json["tryToConnectUser"]
                logger.info(f"User is trying to connect with username: {name}")
                if not websocket_chat_manager.name_taken(name):
                    logger.info(f"Name was not yet taken! Accepting user: {name}")
                    await websocket_chat_manager.connect_username(name, websocket)

                else:
                    await websocket_chat_manager.send_personal_json({"error": "usernameTaken"}, websocket)
            elif "sendChatMessage" in data_json:
                # Client wrote a message
                message_data = data_json["sendChatMessage"]
                author = message_data["author"]
                if websocket_chat_manager.verify(author, websocket):
                    message = message_data["message"]
                    logger.info(f"Broadcasting new message from {author}: {message}")
                    await websocket_chat_manager.broadcast_new_message(
                        ChatMessage(
                            # timestamp=message_data["timestamp"],
                            timestamp=time.time(),
                            author=author,
                            message=message
                        )
                    )

    except WebSocketDisconnect:
        await websocket_chat_manager.disconnect(websocket)
        name = await websocket_chat_manager.disconnect_username(websocket=websocket)
        logger.info(f"Username disconnected: {name}!")


##### END OF WEBSOCKET CHAT


async def background_task_function(my_text: str, other_text: str = " something!"):
    """A background function that gets called once"""
    while 1:
        await asyncio.sleep(60 * 60)
        logger.info(f"Repeated {my_text}{other_text}")


@app.on_event("startup")
async def startup_function():
    asyncio.create_task(background_task_function("hello", other_text=" world!"))
    logger.info("Hello world!")


@app.on_event("shutdown")
async def shutdown_function():
    logger.info("Bye world!")


create_database_if_not_exist()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
