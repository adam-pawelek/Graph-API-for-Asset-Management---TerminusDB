from typing import Union

from fastapi import APIRouter

from terminusApp.views import equipment_crud

from terminusApp import schema

router = APIRouter(
    prefix="/equipment",
    tags=["Equipment"])





@router.get("/")
async def get_equipment(id: Union[str, None] = None):
    return equipment_crud.get_equipment(id)


@router.post("/")
async def create_equipment(item : schema.EquipmentSchema):
    equipment_crud.create_equipment(item)
    return {}


@router.delete("/")
async def delete_equipment(id: Union[str, None] = None):
    return equipment_crud.delete_equipment(id)


@router.put("/")
async def update_equipment(person: schema.EquipmentSchema, id: Union[str, None] = None):
    return equipment_crud.update_equipment(person, id)
