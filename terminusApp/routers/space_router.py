from typing import Union

from fastapi import APIRouter, Security

from terminusApp.auth.utils import get_current_active_user
from terminusApp.service import person_crud, space_crud

from terminusApp import schema, global_crud, models

router = APIRouter(
    prefix="/space",
    tags=["Space"])



@router.get("/all")
async def get_all(current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return global_crud.get_all("Space")



@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Space",id)


@router.post("/")
async def create_space(item : schema.SpaceSchema):
    return space_crud.create_space(item)


@router.put("/add/room")
async def add_room(space_id: Union[str, None] = None,room_id: Union[str, None] = None ):
    return space_crud.add_to_list(space_id,room_id,"room")


@router.delete("/delete/room")
async def remove_room(space_id: Union[str, None] = None,room_id: Union[str, None] = None ):
    return space_crud.remove_from_list(space_id,room_id,"room")



@router.put("/add/equipment")
async def add_equipment(space_id: Union[str, None] = None,equipment_id: Union[str, None] = None ):
    return space_crud.add_to_list(space_id,equipment_id,"equipment")


@router.delete("/delete/equipment")
async def remove_equipment(space_id: Union[str, None] = None,equipment_id: Union[str, None] = None ):
    return space_crud.remove_from_list(space_id,equipment_id,"equipment")


@router.put("/change/reference")
async def change_reference(space_id: Union[str, None] = None,reference_id: Union[str, None] = None ):
    return space_crud.change_reference(space_id,reference_id,)



@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Space",id)


@router.put("/")
async def update_space(space: schema.SpaceSchemaUpdate, id: Union[str, None] = None):
    return space_crud.update_space(space, id)
