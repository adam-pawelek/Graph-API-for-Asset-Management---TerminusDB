
from fastapi import APIRouter, Security

from terminusApp import models
from terminusApp.auth.utils import get_current_active_user
from terminusApp.service import  all


router = APIRouter()

@router.get("/list-all")
async def list_all(current_user: models.User = Security(get_current_active_user, scopes=["admin"])):
    return all.list_all()