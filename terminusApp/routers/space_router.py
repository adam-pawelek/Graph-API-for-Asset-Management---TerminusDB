from typing import Union

from fastapi import APIRouter

from terminusApp.service import person_crud, space_crud

from terminusApp import schema

router = APIRouter(
    prefix="/space",
    tags=["Space"])


@router.get("/")
async def get_schema(id: Union[str, None] = None):
    return space_crud.get_space(id)


@router.post("/")
async def create_person(item : schema.SpaceSchema):
    return space_crud.create_space(item)


@router.delete("/")
async def delete_person(id: Union[str, None] = None):
    return person_crud.delete_person(id)


@router.put("/")
async def update_person(person: schema.SpaceSchema, id: Union[str, None] = None):
    return person_crud.update_person(person, id)
