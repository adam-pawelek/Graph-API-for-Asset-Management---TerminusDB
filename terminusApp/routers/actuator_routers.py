from typing import Union

from fastapi import APIRouter, status

from terminusApp.service import actuator_crud

from terminusApp import schema, global_crud

router = APIRouter(
    prefix="/actuator",
    tags=["Actuator"],
)


@router.get("/all")
async def get_all():
    return global_crud.get_all("Actuator")


@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Actuator",id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_actuator(item : schema.ActuatorSchema, space_id:  Union[str, None] = None):
    actuator_crud.create_actuator(item, space_id)
    return


@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Actuator",id)



@router.put("/")
async def update_actuator(actuator: schema.ActuatorSchemaUpdate,  id: Union[str, None] = None):
    return actuator_crud.update_actuator(actuator,id)
