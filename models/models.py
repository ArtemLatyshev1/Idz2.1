from typing import Union, Annotated

from fastapi import FastAPI
from pydantic import BaseModel, Field

class User(BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None

class UserDB(User):
    password: Annotated[Union[str, None], Field(max_length=35, min_length=5)] = None

class Directory(BaseModel):
    massage: str
