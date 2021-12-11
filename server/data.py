from pydantic import BaseModel


mensajes: "list[Mensaje]" = []


class Mensaje(BaseModel):
    autor: str
    contenido: str
