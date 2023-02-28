from typing import Union

from fastapi import APIRouter, Security, Depends

from terminusApp.auth.utils import get_current_active_user, get_current_user
from terminusApp.service import person_crud

from terminusApp import schema, global_crud, models

router = APIRouter(
    prefix="/person",
    tags=["Person"])



@router.get("/all")
async def get_all(current_user: models.User = Depends(get_current_user)):
    return global_crud.get_all("Person")

@router.get("/")
async def get(id: Union[str, None] = None, current_user: models.User = Depends(get_current_user)):
    return global_crud.get("Person",id)


@router.post("/")
async def create_person(item : schema.PersonSchema, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    person_crud.create_person(item)
    return {}


@router.delete("/")
async def delete(id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return global_crud.delete("Person",id)


@router.put("/")
async def update_person(person: schema.PersonSchema, id: Union[str, None] = None, current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return person_crud.update_person(person, id)
