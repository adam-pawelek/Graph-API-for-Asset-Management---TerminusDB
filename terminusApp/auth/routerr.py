###############################
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jose import JWTError, jwt
from passlib.context import CryptContext


from datetime import datetime, timedelta
from typing import List, Union
from fastapi import FastAPI, APIRouter
from fastapi import Depends, HTTPException, status, Security
from pydantic import BaseModel, ValidationError


from terminusApp.auth.models import Token, TokenData




# to get a string like this run:
# openssl rand -hex 32
from terminusApp import views, models
from terminusApp.auth.utils import pwd_context, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, \
    get_current_active_user, get_current_user

router = APIRouter()



#class UserInDB(User):
#    hashed_password: str





@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user( form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/")
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user.email

@router.get("/users/me/items/")
async def read_own_items(
    current_user: models.User = Security(get_current_active_user, scopes=["items"])
):
    return [{"item_id": "Foo", "owner": current_user.email}]


@router.get("/status/")
async def read_system_status(current_user: models.User = Depends(get_current_user)):
    return {"status": "ok"}