import json

from fastapi import FastAPI

from terminusdb_client import Client, WOQLClient, WOQLSchema
from terminusdb_client.schema import Schema, DocumentTemplate, RandomKey
from typing import Union, Set, List

from models import my_schema, Pet


from database import client

import  crud

from routers import all,pet



try:
    client.create_database("MyDatabase")
except:
    pass


my_schema.commit(client)



app = FastAPI()


app.include_router(all.router)

app.include_router(pet.router)


'''
@app.get("/list-all")
async def list_all():
    return crud.list_all()

'''


'''
@app.post("/add-player")
async def say_hello(item :Item):
    my_dog = Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    my_player = Player(name='kkkkk',age=10,weight= 10.0,pets = [my_dog] )
    client.insert_document([my_player])


    return {"message": f"Hello {item}"}

'''

'''



@app.put("/kkkk")
async def root():
    sth = (list(client.get_all_documents()))
    print ("asdfasdf")
    doc_id = sth[0]["@id"]
    cos = client.get_document(doc_id)
    my_dog = {}
    cos["name"] = "update"
    cos["species"] = "ll"
    cos["age"] = 1
    cos["weight"] =12
    print(my_dog)

    #my_dog = PetSchema(name="asdf", species="asdfas", age=10, weight=12)
    #my_dog = json.dumps(my_dog.__dict__,cls=MyEncoder)

    query = client.replace_document(cos)

   # client.update(query)

    return {}



'''