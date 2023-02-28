from typing import Union

from fastapi import APIRouter

from terminusApp.service import sensor_crud

from terminusApp import schema

router = APIRouter(
    prefix="/sensor",
    tags=["Sensor"])


@router.get("/")
async def get_sensor(id: Union[str, None] = None):
    return sensor_crud.get_sensor(id)


@router.post("/")
async def create_sensor(item : schema.SensorSchema, space_id:  Union[str, None] = None):
    sensor_crud.create_sensor(item, space_id)
    return {}


@router.delete("/")
async def delete_sensor(id: Union[str, None] = None):
    return sensor_crud.delete_sensor(id)



@router.put("/")
async def update_sensor(sensor: schema.SensorSchemaUpdate,  id: Union[str, None] = None):
    return sensor_crud.update_sensor(sensor,id)
