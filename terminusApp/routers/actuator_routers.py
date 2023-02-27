from typing import Union

from fastapi import APIRouter

from terminusApp.views import actuator_crud

from terminusApp import schema

router = APIRouter(tags=["Actuator"])


@router.get("/get-actuator")
async def get_actuator(id: Union[str, None] = None):
    return actuator_crud.get_actuator(id)


@router.post("/add-actuator")
async def create_actuator(item : schema.ActuatorSchema, space_id:  Union[str, None] = None):
    actuator_crud.create_actuator(item, space_id)
    return {}


@router.delete("/delete-actuator")
async def delete_actuator(id: Union[str, None] = None):
    return actuator_crud.delete_actuator(id)


'''
@router.put("/update-actuator")
async def update_actuator(person: schema.EquipmentSchema,  id: Union[str, None] = None):
    return actuator_crud.update_equipment(person,id)
'''