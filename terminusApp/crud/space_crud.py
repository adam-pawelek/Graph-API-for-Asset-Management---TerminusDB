from terminusApp import models, schema
from terminusApp.database import client

from terminusApp.crud import person_crud, equipment_crud


def get_space(id):
    space = client.get_document(id)
    return space





def create_space(space_schema : schema.SpaceSchema):
    equipment = []
    for equipmentSchema in space_schema.equipment:
        equipment.append(equipment_crud.create_equipment(equipmentSchema))

    person = person_crud.create_person(space_schema.reference)
    space = models.Space(label = space_schema.label, type = space_schema.type, capacity = space_schema.capacity, room = [], reference = person, equipment =equipment)
    client.insert_document([space])
    return {"message": f"Hello {space_schema}"}




def delete_space(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))




def update_space(new_person : schema.PersonSchema, id):
    current_person = client.get_document(id)
    current_person["name"] = new_person.name
    current_person["surname"] = new_person.surname
    query = client.replace_document(current_person)

    return {}
    
