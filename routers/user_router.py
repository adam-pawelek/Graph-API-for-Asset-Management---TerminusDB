import json
from typing import Union

from fastapi import APIRouter

from crud import  user_crud

import schema

router = APIRouter()


@router.get("/get-user")
async def get_user(id: Union[str, None] = None):
    return user_crud.get_noraml_user(id)

@router.get("/get-email")
async def get_us(email: Union[str, None] = None):
    return user_crud.get_user_by_email(email).email


@router.post("/add-user")
async def create_user(item :schema.UserSchema):
    return user_crud.create_normal_user(item)


@router.delete("/delete-user")
async def delete_user(id: Union[str, None] = None):
    return user_crud.delete_noraml_user(id)


@router.put("/update-user")
async def update_user(user: schema.UserSchema,  id: Union[str, None] = None):
    return user_crud.update_normal_user(user,id)
