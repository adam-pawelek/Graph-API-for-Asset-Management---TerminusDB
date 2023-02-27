from typing import Union

from fastapi import APIRouter

from terminusApp.crud import person_crud, space_crud

from terminusApp import schema

router = APIRouter(tags=["Space"])


@router.get("/get-space")
async def get_schema(id: Union[str, None] = None):
    return space_crud.get_space(id)


@router.post("/add-space")
async def create_person(item : schema.SpaceSchema):
    return space_crud.create_space(item)


@router.delete("/delete-space")
async def delete_person(id: Union[str, None] = None):
    return person_crud.delete_person(id)


@router.put("/update-space")
async def update_person(person: schema.SpaceSchema, id: Union[str, None] = None):
    return person_crud.update_person(person, id)
