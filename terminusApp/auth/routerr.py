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
from terminusApp import service, models
from terminusApp.auth.utils import pwd_context, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, \
    get_current_active_user, get_current_user

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user( form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if "admin" in form_data.scopes and user.role != "admin":
        print("www")
        print(user.role)
        raise HTTPException(status_code=401, detail="No admin")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

