from terminusApp import models, schema
from terminusApp.database import client



def get_person(id):
    person = client.get_document(id)
    return person



def create_person(person_schema : schema.PersonSchema):
    person = models.Person(name=person_schema.name, surname = person_schema.surname)
    client.insert_document([person])
    return person




def delete_person(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))




def update_person(new_person : schema.PersonSchema, id):
    current_person = client.get_document(id)
    current_person["name"] = new_person.name
    current_person["surname"] = new_person.surname
    query = client.replace_document(current_person)

    return {}
