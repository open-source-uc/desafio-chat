from fastapi import WebSocket

from contextlib import asynccontextmanager

from .data import Mensaje, mensajes


class ConfectionHandler:
    "Maneja las conexiones de WebSockets"

    def __init__(self) -> None:
        self.connections: "set[WebSocket]" = set()

    @asynccontextmanager
    async def connect(self, connection: WebSocket):
        self.connections.add(connection)
        try:
            yield self
        finally:
            self.connections.remove(connection)


async def handle_socket(socket: WebSocket, connections: "set[WebSocket]"):
    data = await socket.receive_json()
    try:
        mensaje = Mensaje.parse_obj(data)
        mensajes.append(mensaje)
        for connection in connections:
            await connection.send_text(mensaje.json())
    except Exception as error:
        print(error)
