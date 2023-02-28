from datetime import datetime

from pydantic import BaseModel
from typing import List






class PersonSchema(BaseModel):
    name: str
    surname: str


class EquipmentSchema(BaseModel):
    label: str
    type: str
    ports_numer: int
    capacity: float # optional



class SpaceSchema(BaseModel):
    label: str
    type: str
    capacity: int   # optional
    #room: List [Space]
    reference: PersonSchema
    equipment: List[EquipmentSchema]


class SensorSchema(BaseModel):
    label: str
    type: str
    fw_version: str
    hw_version: float # optional
    installation_date: datetime
    sensor_location: SpaceSchema


class SensorSchemaUpdate(BaseModel):
    label: str
    type: str
    fw_version: str
    hw_version: float # optional
    installation_date: datetime
    #sensor_location: SpaceSchema


class ActuatorSchema(BaseModel):
    id: str
    label: str
    type: str
    hw_version: float
    installation_date: datetime
    gateway_location: SpaceSchema
    powered: List[EquipmentSchema]
    network_link: List[EquipmentSchema]




class LogicSchema (BaseModel):
    label: str
    type: str
    use_case: SpaceSchema




class LogicSchemaUpdate (BaseModel):
    label: str
    type: str



class PlaceSchema(BaseModel):
    label: str
    type: str
    location: List[SpaceSchema]

class PlaceSchemaUpdate(BaseModel):
    label: str
    type: str





class UserSchema(BaseModel):
    name: str
    surname: str
    email: str
    password: str
#    role: str  # admin, user




