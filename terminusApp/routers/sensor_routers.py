from typing import Union

from fastapi import APIRouter

from terminusApp.views import sensor_crud

from terminusApp import schema

router = APIRouter(tags=["Sensor"])


@router.get("/get-sensor")
async def get_actuator(id: Union[str, None] = None):
    return sensor_crud.get_sensor(id)


@router.post("/add-sensor")
async def create_actuator(item : schema.SensorSchema, space_id:  Union[str, None] = None):
    sensor_crud.create_sensor(item, space_id)
    return {}


@router.delete("/delete-sensor")
async def delete_actuator(id: Union[str, None] = None):
    return sensor_crud.delete_sensor(id)


'''
@router.put("/update-actuator")
async def update_actuator(person: schema.EquipmentSchema,  id: Union[str, None] = None):
    return actuator_crud.update_equipment(person,id)
'''