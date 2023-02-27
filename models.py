from datetime import datetime

from terminusdb_client import DocumentTemplate, WOQLSchema
from typing import Set, List


my_schema = WOQLSchema()

class Pet(DocumentTemplate):
    _schema = my_schema
    name: str
    species: str
    age: int
    weight: float


class Person(DocumentTemplate):
    _schema = my_schema
    name: str
    surname: str


class Space(DocumentTemplate):
    _schema = my_schema
    label: str
    type: str
    capacity: int   # optional
    room: List ['Space']
    reference: Person
    equipment: List['Equipment']


class Sensor(DocumentTemplate):
    _schema = my_schema
    id: str
    label: str
    type: str
    fw_version: str
    hw_version: float # optional
    installation_date: datetime
    sensor_location: Space


class Actuator(DocumentTemplate):
    _schema = my_schema
    id: str
    label: str
    type: str
    hw_version: float
    installation_date: datetime
    gateway_location: Space
    powered: List['Equipment']
    network_link: List['Equipment']


class Equipment(DocumentTemplate):
    _schema = my_schema
    label: str
    type: str
    ports_numer: int
    capacity: float # optional


class Logic (DocumentTemplate):
    _schema = my_schema
#    id: str
    label: str
    type: str
    use_case: Space



class Place(DocumentTemplate):
    _schema = my_schema
    id: str
    label: str
    type: str
    location: List['Space']





class User(DocumentTemplate):
    _schema = my_schema
    name: str
    surname: str
    email: str
    password: str
    role: str  # admin, user







