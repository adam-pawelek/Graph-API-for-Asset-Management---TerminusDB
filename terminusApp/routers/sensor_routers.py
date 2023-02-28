from typing import Union

from fastapi import APIRouter, Security

from terminusApp.auth.utils import get_current_active_user
from terminusApp.service import sensor_crud

from terminusApp import schema, global_crud, models

router = APIRouter(
    prefix="/sensor",
    tags=["Sensor"])


@router.get("/all")
async def get_all(current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
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



@router.put("/change/sensor_location")
async def change_use_case(main_id: Union[str, None] = None,change_id: Union[str, None] = None ):
    return global_crud.change_attribute(main_id,change_id,"sensor_location")