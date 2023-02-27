from fastapi import FastAPI
from terminusApp.routers import all, person_router, equipment_routers, user_router, logic_router, place_routers, sensor_routers
from terminusApp import auth
from terminusApp.routers import space_router, actuator_routers

from terminusApp.models import my_schema
from terminusApp.database import client
import terminusApp.auth.routerr


try:
    client.create_database("MyDatabase")
except:
    pass


my_schema.commit(client)


app = FastAPI()

app.include_router(all.router)
app.include_router(person_router.router)
app.include_router(equipment_routers.router)
app.include_router(user_router.router)
app.include_router(space_router.router)
app.include_router(logic_router.router)
app.include_router(place_routers.router)
app.include_router(actuator_routers.router)
app.include_router(sensor_routers.router)
app.include_router(auth.routerr.router)




########################

'''
@terminusApp.post("/add-player")
async def say_hello(item :Item):
    my_dog = Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    my_player = Player(name='kkkkk',age=10,weight= 10.0,pets = [my_dog] )
    client.insert_document([my_player])


    return {"message": f"Hello {item}"}

'''

