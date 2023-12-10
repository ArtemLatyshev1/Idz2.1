from fastapi import APIRouter, Body
from models.models import User, UserDB, Directory
from typing import Union, Annotated

users_router = APIRouter()

def coder_password(cod: str):
    result = cod*2

users_list = [UserDB(name='Ivanov', id = 108, password = '******'), UserDB(name='Petrov', id = 100, password = '*******')]

def find_user(id:int) -> Union[UserDB, None]:
    for user in users_list:
        if user.id == id:
            return user
    return None

@users_router.get("/api/users)", response_model=Union[list[User], None])
def get_users():
    return users_list

@users_router.get("/api/users/{id})", response_model=Union[User, Directory])
def get_users(id: int):
    user = find_user(id)
    print(user)
    if (user == None):
        return Directory(massage= "Такой пользователь не найден")
    return user

@users_router.post("/api/users)", response_model=Union[User, Directory])
def create_user(item: Annotated[User, Body(embed=True, description="Новый пользователь")]):
    user = UserDB(name = item.name, id = item.id, password = coder_password(item.name))
    users_list.append(user)
    return user

@users_router.put("/api/users/{id})", response_model=Union[User, Directory])
def edit_person(item: Annotated[User, Body(embed=True, description="Изменяем данные пользователя по id")]):
    user = find_user(item.id)
    if (user == None):
        return Directory(massage= "Такой пользователь не найден")
    user.id = item.id
    user.name = item.name
    return user

@users_router.delete("/api/users/{id})", response_model=Union[list[User], None])
def delete_person(id: int):
    user = find_user(id)
    if (user == None):
        return Directory(massage= "Такой пользователь не найден")
    users_list.remove(user)
    return users_list
