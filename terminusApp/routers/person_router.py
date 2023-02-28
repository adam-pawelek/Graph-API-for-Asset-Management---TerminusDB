from typing import Union

from fastapi import APIRouter

from terminusApp.service import person_crud

from terminusApp import schema, global_crud

router = APIRouter(
    prefix="/person",
    tags=["Person"])



@router.get("/all")
async def get_all():
    return global_crud.get_all("Person")

@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Person",id)


@router.post("/")
async def create_person(item : schema.PersonSchema):
    person_crud.create_person(item)
    return {}


@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Person",id)


@router.put("/")
async def update_person(person: schema.PersonSchema, id: Union[str, None] = None):
    return person_crud.update_person(person, id)
