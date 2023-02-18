import json

from fastapi import FastAPI
from pydantic import BaseModel
from terminusdb_client import Client, WOQLClient, WOQLSchema
from terminusdb_client.schema import Schema, DocumentTemplate, RandomKey
from typing import Union, Set, List

from database import my_schema



client = WOQLClient("http://127.0.0.1:6363/")
client.connect()
try:
    client.create_database("MyDatabase")
except:
    pass


'''
class Player(DocumentTemplate):
    _schema = my_schema
    name: str
    age: int
    weight: float
    friend_of: Set ['Pet']
'''









my_schema.commit(client)



app = FastAPI()




class Item(BaseModel):
    name: str
    species: str
    age: int
    weight: float






@app.get("/list-all")
async def root():
    #sth = (list(client.get_all_documents()))
    #print ("asdfasdf")
    #doc_id = sth[0]["@id"]
    #client.delete_document(doc_id)
    return (list(client.get_all_documents()))

'''
@app.post("/add-player")
async def say_hello(item :Item):
    my_dog = Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    my_player = Player(name='kkkkk',age=10,weight= 10.0,pets = [my_dog] )
    client.insert_document([my_player])


    return {"message": f"Hello {item}"}

'''

@app.post("/add-pet")
async def say_hello(item :Item):
    my_dog = Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    client.insert_document([my_dog])


    return {"message": f"Hello {item}"}



@app.delete("/wwww")
async def root():
    sth = (list(client.get_all_documents()))
    print ("asdfasdf")
    doc_id = sth[0]["@id"]
    client.delete_document(doc_id)
    return (list(client.get_all_documents()))




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

    #my_dog = Pet(name="asdf", species="asdfas", age=10, weight=12)
    #my_dog = json.dumps(my_dog.__dict__,cls=MyEncoder)

    query = client.replace_document(cos)

   # client.update(query)

    return {}



