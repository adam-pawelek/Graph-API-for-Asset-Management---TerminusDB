from typing import Union, List

from fastapi import APIRouter

from terminusApp.service import place_crud

from terminusApp import schema, global_crud

router = APIRouter(
    prefix="/place",
    tags=["Place"])



@router.get("/all")
async def get_all():
    return global_crud.get_all("Place")


@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Place",id)


@router.post("/")
async def create_place(item : schema.PlaceSchema, id_spaces: List[Union[str, None]]):
    place_crud.create_place(item, id_spaces)
    return {}



@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Place",id)


@router.put("/update-logic")
async def update_place(person: schema.PlaceSchemaUpdate,  id: Union[str, None] = None):
    return place_crud.update_place(person,id)
