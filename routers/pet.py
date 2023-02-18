from typing import Union

from fastapi import APIRouter

from crud import  pet

import schema

router = APIRouter()


@router.get("/get-pet")
async def get_pet(id: Union[str, None] = None):
    return pet.get_pet(id)



@router.post("/add-pet")
async def say_hello(item :schema.PetSchema):
    return pet.create_pet(item)




@router.delete("/wwww")
async def root():
    return pet.delete_pet()


@router.put("/kkkk")
async def root():

    return pet.update_pet()
