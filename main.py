from fastapi import FastAPI
from models import my_schema, Pet
from database import client
from routers import all,pet_router, person_router, equipment_routers, user_router

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



'''
@app.post("/add-player")
async def say_hello(item :Item):
    my_dog = Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    my_player = Player(name='kkkkk',age=10,weight= 10.0,pets = [my_dog] )
    client.insert_document([my_player])


    return {"message": f"Hello {item}"}

'''

