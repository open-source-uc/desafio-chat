from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from .data import mensajes
from .websockets import ConfectionHandler, handle_socket

app = FastAPI()

app.mount("/client", StaticFiles(directory="client", html=True), name="client")


@app.get("/")
async def index():
    return RedirectResponse("client/")


@app.get("/mensajes")
async def lista_mensajes():
    return mensajes


handler = ConfectionHandler()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    async with handler.connect(websocket):
        while True:
            await handle_socket(websocket, handler.connections)
