from typing import Union

from fastapi import APIRouter, Security, Depends

from terminusApp.auth.utils import get_current_active_user, get_current_user
from terminusApp.service import equipment_crud

from terminusApp import schema, models

from terminusApp import global_crud

router = APIRouter(
    prefix="/equipment",
    tags=["Equipment"])





@router.get("/")
async def get(id: Union[str, None] = None, current_user: models.User = Depends(get_current_user)):
    return global_crud.get("Equipment",id)


@router.get("/all")
async def get_all_equipment(current_user: models.User = Depends(get_current_user)):
    return global_crud.get_all("Equipment")

@router.post("/")
async def create_equipment(item : schema.EquipmentSchema, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    equipment_crud.create_equipment(item)
    return {}


@router.delete("/")
async def delete(id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return global_crud.delete("Equipment",id)


@router.put("/")
async def update_equipment(person: schema.EquipmentSchema, id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return equipment_crud.update_equipment(person, id)
