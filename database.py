from datetime import datetime

from terminusdb_client import DocumentTemplate
from typing import Set, List



class Person(DocumentTemplate):
    id: str
    name: str
    surname: str

class Space(DocumentTemplate):
    _schema = my_schema
    id: str
    label: str
    type: str
    capacity: int   # optional
    room: List ['Space']
    reference: Person
    equipment: List['Equipment']


class Sensor(DocumentTemplate):
    id: str
    label: str
    type: str
    fw_version: str
    hw_version: float # optional
    installation_date: datetime
    sensor_location = Space


class Actuator(DocumentTemplate):
    id: str
    label: str
    type: str
    hw_version: float
    installation_date: datetime
    gateway_location = Space
    powered = List['Equipment']
    network_link = List['Equipment']


class Equipment(DocumentTemplate):
    id: str
    label: str
    type: str
    ports_numer: int
    capacity: float # optional


class Logic (DocumentTemplate):
    id: str
    label: str
    type: str
    use_case: Space



class Place(DocumentTemplate):
    id: str
    label: str
    type: str
    location: List['Space']





class User(DocumentTemplate):
    id: str
    name: str
    surname: str
    email: str
    password: str
    role: str  # admin, user






