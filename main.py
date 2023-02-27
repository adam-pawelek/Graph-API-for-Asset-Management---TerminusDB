from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import crud.user_crud
from models import my_schema, Pet
from database import client
from routers import all,pet_router, person_router, equipment_routers, user_router, space_router, logic_router

import  models
import schema
############
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
############

try:
    client.create_database("MyDatabase")
except:
    pass


my_schema.commit(client)



app = FastAPI()


app.include_router(all.router)

app.include_router(pet_router.router)

app.include_router(person_router.router)

app.include_router(equipment_routers.router)

app.include_router(user_router.router)

app.include_router(space_router.router)

app.include_router(logic_router.router)

###############################

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

#class UserInDB(User):
#    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(email: str):
    return crud.user_crud.get_user_by_email(email)



def authenticate_user (email: str, password: str):
    user = get_user(email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user



########################

'''
@app.post("/add-player")
async def say_hello(item :Item):
    my_dog = Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    my_player = Player(name='kkkkk',age=10,weight= 10.0,pets = [my_dog] )
    client.insert_document([my_player])


    return {"message": f"Hello {item}"}

'''

