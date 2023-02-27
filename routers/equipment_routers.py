from typing import Union

from fastapi import APIRouter

from crud import  equipment_crud

import schema

router = APIRouter(tags=["Equipment"])


@router.get("/get-equipment")
async def get_equipment(id: Union[str, None] = None):
    return equipment_crud.get_equipment(id)


@router.post("/add-equipment")
async def create_equipment(item :schema.EquipmentSchema):
    equipment_crud.create_equipment(item)
    return {}


@router.delete("/delete-equipment")
async def delete_equipment(id: Union[str, None] = None):
    return equipment_crud.delete_equipment(id)


@router.put("/update-equipment")
async def update_equipment(person: schema.EquipmentSchema,  id: Union[str, None] = None):
    return equipment_crud.update_equipment(person,id)
