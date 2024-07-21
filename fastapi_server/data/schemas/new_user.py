from pydantic import BaseModel


class NewUser(BaseModel):
    name: str
    job: str


class NewUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str
