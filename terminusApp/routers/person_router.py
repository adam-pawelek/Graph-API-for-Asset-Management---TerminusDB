from typing import Union

from fastapi import APIRouter

from terminusApp.views import person_crud

from terminusApp import schema

router = APIRouter(
    prefix="/person",
    tags=["Person"])


@router.get("/")
async def get_person(id: Union[str, None] = None):
    return person_crud.get_person(id)


@router.post("/")
async def create_person(item : schema.PersonSchema):
    person_crud.create_person(item)
    return {}


@router.delete("/")
async def delete_person(id: Union[str, None] = None):
    return person_crud.delete_person(id)


@router.put("/")
async def update_person(person: schema.PersonSchema, id: Union[str, None] = None):
    return person_crud.update_person(person, id)
