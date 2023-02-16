from fastapi import FastAPI
from pydantic import BaseModel
from terminusdb_client import Client
from terminusdb_client.schema import Schema, DocumentTemplate, RandomKey
from typing import Union

client = Client("http://127.0.0.1:6363/")
client.connect()
try:
    client.create_database("MyDatabase")
except:
    pass

my_schema = Schema()

class Pet(DocumentTemplate):
    _schema = my_schema
    name: str
    species: str
    age: int
    weight: float

my_schema.commit(client)



app = FastAPI()




class Item(BaseModel):
    name: str
    species: str
    age: int
    weight: float


@app.get("/list-all")
async def root():
    return (list(client.get_all_documents()))


@app.post("/add-pet")
async def say_hello(item :Item):
    my_dog = Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    client.insert_document([my_dog])

    return {"message": f"Hello {item}"}
