from typing import Union

from fastapi import APIRouter

from terminusApp.service import sensor_crud

from terminusApp import schema, global_crud

router = APIRouter(
    prefix="/sensor",
    tags=["Sensor"])


@router.get("/all")
async def get_all():
    return global_crud.get_all("Sensor")


@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Sensor",id)


@router.post("/")
async def create_sensor(item : schema.SensorSchema, space_id:  Union[str, None] = None):
    sensor_crud.create_sensor(item, space_id)
    return {}


@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Sensor",id)



@router.put("/")
async def update_sensor(sensor: schema.SensorSchemaUpdate,  id: Union[str, None] = None):
    return sensor_crud.update_sensor(sensor,id)
