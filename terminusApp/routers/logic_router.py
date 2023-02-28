from typing import Union

from fastapi import APIRouter

from terminusApp.service import logic_crud

from terminusApp import schema, global_crud

router = APIRouter(
    prefix="/logic",
    tags=["Logic"])



@router.get("/all")
async def get_all_logic():
    return global_crud.get_all("Logic")


@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Logic",id)


@router.post("/")
async def create_logic(item : schema.LogicSchema, id_space: Union[str, None] = None):
    logic_crud.create_logic(item, id_space)
    return {}



@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Logic",id)



@router.put("/change/use-case")
async def change_use_case(logic_id: Union[str, None] = None,use_case_id: Union[str, None] = None ):
    return logic_crud.change_use_case(logic_id,use_case_id,)



@router.put("/")
async def update_logic(person: schema.LogicSchemaUpdate,  id: Union[str, None] = None):
    return logic_crud.update_logic(person,id)
