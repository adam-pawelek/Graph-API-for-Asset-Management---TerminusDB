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




