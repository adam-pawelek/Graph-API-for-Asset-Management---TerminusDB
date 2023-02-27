from typing import Union

from fastapi import APIRouter

from terminusApp.views import user_crud

from terminusApp import schema

router = APIRouter(
    prefix="/user",
    tags=["User"])


@router.get("/normal")
async def get_user(id: Union[str, None] = None):
    return user_crud.get_noraml_user(id)

@router.get("/normal/email")
async def get_us(email: Union[str, None] = None):
    return user_crud.get_user_by_email(email).email


@router.post("/normal")
async def create_user(item : schema.UserSchema):
    return user_crud.create_normal_user(item)

@router.post("/admin")
async def create_admin_user(item : schema.UserSchema):
    return user_crud.create_admin_user(item)


@router.delete("/normal")
async def delete_user(id: Union[str, None] = None):
    return user_crud.delete_noraml_user(id)


@router.put("/normal")
async def update_user(user: schema.UserSchema, id: Union[str, None] = None):
    return user_crud.update_normal_user(user, id)
