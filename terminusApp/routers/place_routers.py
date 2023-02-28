from typing import Union, List

from fastapi import APIRouter, Security, Depends

from terminusApp.auth.utils import get_current_active_user, get_current_user
from terminusApp.service import place_crud

from terminusApp import schema, global_crud, models

router = APIRouter(
    prefix="/place",
    tags=["Place"])



@router.get("/all")
async def get_all(current_user: models.User = Depends(get_current_user)):
    return global_crud.get_all("Place")


@router.get("/")
async def get(id: Union[str, None] = None, current_user: models.User = Depends(get_current_user)):
    return global_crud.get("Place",id)


@router.post("/")
async def create_place(item : schema.PlaceSchema, id_spaces: List[Union[str, None]], current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    place_crud.create_place(item, id_spaces)
    return {}



@router.delete("/")
async def delete(id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return global_crud.delete("Place",id)


@router.put("/")
async def update_place(person: schema.PlaceSchemaUpdate,  id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return place_crud.update_place(person,id)



@router.put("/add/location")
async def add_location(main_id: Union[str, None] = None, change_id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return global_crud.add_to_list(main_id, change_id, "location")


@router.delete("/delete/location")
async def remove_location(space_id: Union[str, None] = None,equipment_id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"]) ):
    return global_crud.remove_from_list(space_id,equipment_id,"location")