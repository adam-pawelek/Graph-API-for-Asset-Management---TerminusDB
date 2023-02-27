from typing import Union

from fastapi import APIRouter

from terminusApp.crud import pet_crud

from terminusApp import schema

router = APIRouter(tags=["Pet"])


@router.get("/get-pet")
async def get_pet(id: Union[str, None] = None):
    return pet_crud.get_pet(id)


@router.post("/add-pet")
async def say_hello(item : schema.PetSchema):
    return pet_crud.create_pet(item)


@router.delete("/delete-pet")
async def delete_pet(id: Union[str, None] = None):
    return pet_crud.delete_pet(id)


@router.put("/update-pet")
async def update_pet(pet: schema.PetSchema, id: Union[str, None] = None):
    return pet_crud.update_pet(pet, id)
