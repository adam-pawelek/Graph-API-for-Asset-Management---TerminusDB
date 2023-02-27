from typing import Union, List

from fastapi import APIRouter

from terminusApp.crud import place_crud

from terminusApp import schema

router = APIRouter(tags=["Place"])


@router.get("/get-place")
async def get_place(id: Union[str, None] = None):
    return place_crud.get_place(id)


@router.post("/add-place")
async def create_place(item : schema.PlaceSchema, id_spaces: List[Union[str, None]]):
    place_crud.create_place(item, id_spaces)
    return {}



@router.delete("/delete-place")
async def delete_place(id: Union[str, None] = None):
    return place_crud.delete_place(id)

'''
@router.put("/update-logic")
async def update_logic(person: schema.PersonSchema,  id: Union[str, None] = None):
    return logic_crud.up(person,id)
'''