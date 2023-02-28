from typing import Union

from fastapi import APIRouter

from terminusApp.service import equipment_crud

from terminusApp import schema

from terminusApp import global_crud

router = APIRouter(
    prefix="/equipment",
    tags=["Equipment"])





@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Equipment",id)


@router.get("/all")
async def get_all_equipment():
    return global_crud.get_all("Equipment")

@router.post("/")
async def create_equipment(item : schema.EquipmentSchema):
    equipment_crud.create_equipment(item)
    return {}


@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Equipment",id)


@router.put("/")
async def update_equipment(person: schema.EquipmentSchema, id: Union[str, None] = None):
    return equipment_crud.update_equipment(person, id)
