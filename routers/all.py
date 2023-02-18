
from fastapi import APIRouter

from crud import  all


router = APIRouter()

@router.get("/list-all")
async def list_all():
    return all.list_all()