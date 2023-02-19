from typing import Union

from fastapi import APIRouter

from crud import  person_crud

import schema

router = APIRouter()


@router.get("/get-person")
async def get_person(id: Union[str, None] = None):
    return person_crud.get_person(id)


@router.post("/add-person")
async def create_person(item :schema.PersonSchema):
    return person_crud.create_person(item)


@router.delete("/delete-person")
async def delete_person(id: Union[str, None] = None):
    return person_crud.delete_person(id)


@router.put("/update-person")
async def update_person(person: schema.PersonSchema,  id: Union[str, None] = None):
    return person_crud.update_person(person,id)
