from pydantic import BaseModel


class ServerData(BaseModel):
    server: str
