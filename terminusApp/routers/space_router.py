from typing import Union

from fastapi import APIRouter

from terminusApp.service import person_crud, space_crud

from terminusApp import schema, global_crud

router = APIRouter(
    prefix="/space",
    tags=["Space"])



@router.get("/all")
async def get_all():
    return global_crud.get_all("Space")



@router.get("/")
async def get(id: Union[str, None] = None):
    return global_crud.get("Space",id)


@router.post("/")
async def create_space(item : schema.SpaceSchema):
    return space_crud.create_space(item)


@router.put("/add/room")
async def create_space(space_id: Union[str, None] = None,room_id: Union[str, None] = None ):
    return space_crud.add_room(space_id,room_id)


@router.delete("/delete/room")
async def create_space(space_id: Union[str, None] = None,room_id: Union[str, None] = None ):
    return space_crud.remove_room(space_id,room_id)

@router.delete("/")
async def delete(id: Union[str, None] = None):
    return global_crud.delete("Space",id)


@router.put("/")
async def update_space(space: schema.SpaceSchemaUpdate, id: Union[str, None] = None):
    return space_crud.update_space(space, id)
