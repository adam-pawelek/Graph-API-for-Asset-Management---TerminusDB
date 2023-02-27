from typing import Union, List

from fastapi import APIRouter

from terminusApp.service import place_crud

from terminusApp import schema

router = APIRouter(
    prefix="/place",
    tags=["Place"])


@router.get("/")
async def get_place(id: Union[str, None] = None):
    return place_crud.get_place(id)


@router.post("/")
async def create_place(item : schema.PlaceSchema, id_spaces: List[Union[str, None]]):
    place_crud.create_place(item, id_spaces)
    return {}



@router.delete("/")
async def delete_place(id: Union[str, None] = None):
    return place_crud.delete_place(id)


@router.put("/update-logic")
async def update_place(person: schema.PlaceSchemaUpdate,  id: Union[str, None] = None):
    return place_crud.update_place(person,id)
