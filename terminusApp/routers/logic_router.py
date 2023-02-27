from typing import Union

from fastapi import APIRouter

from terminusApp.views import logic_crud

from terminusApp import schema

router = APIRouter(
    prefix="/logic",
    tags=["Logic"])


@router.get("/")
async def get_logic(id: Union[str, None] = None):
    return logic_crud.get_logic(id)


@router.post("/")
async def create_logic(item : schema.LogicSchema, id_space: Union[str, None] = None):
    logic_crud.create_logic(item, id_space)
    return {}



@router.delete("/")
async def delete_logic(id: Union[str, None] = None):
    return logic_crud.delete_logic(id)

'''
@router.put("/update-logic")
async def update_logic(person: schema.PersonSchema,  id: Union[str, None] = None):
    return logic_crud.up(person,id)
'''