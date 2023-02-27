from typing import Union

from fastapi import APIRouter, status

from terminusApp.service import actuator_crud

from terminusApp import schema

router = APIRouter(
    prefix="/actuator",
    tags=["Actuator"],
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_actuator(id: Union[str, None] = None):
    return actuator_crud.get_actuator(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_actuator(item : schema.ActuatorSchema, space_id:  Union[str, None] = None):
    actuator_crud.create_actuator(item, space_id)
    return


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_actuator(id: Union[str, None] = None):
    actuator_crud.delete_actuator(id)
    return


'''
@router.put("/update-actuator")
async def update_actuator(person: schema.EquipmentSchema,  id: Union[str, None] = None):
    return actuator_crud.update_equipment(person,id)
'''