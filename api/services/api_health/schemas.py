from pydantic import BaseModel


class ResponseHealthStatus(BaseModel):
    status: str
