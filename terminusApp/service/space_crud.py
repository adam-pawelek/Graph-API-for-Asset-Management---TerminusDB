from fastapi import HTTPException, status

from terminusApp import models, schema
from terminusApp.database import client

from terminusApp.service import person_crud, equipment_crud


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




def update_space(new_space : schema.SpaceSchemaUpdate, id):
    current_space = client.get_document(id)
    current_space["type"] = new_space.type
    current_space["label"] = new_space.label
    current_space["capacity"] = new_space.capacity
    query = client.replace_document(current_space)

    return {}


def add_to_list(space_id, room_id,type):
    try:
        space = client.get_document(space_id)
        room = client.get_document(room_id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")
    if room_id in space[type]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Room already in space")

    space[type].append(room_id)
    query = client.replace_document(space)
    return

def remove_from_list(space_id, room_id, type):
    try:
        space = client.get_document(space_id)
        room = client.get_document(room_id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")
    if room_id not in space[type]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")

    space[type].remove(room_id)
    query = client.replace_document(space)
    return


def change_reference(id, person_id):
    try:
        current_space = client.get_document(id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")
    current_space["reference"] = person_id
    query = client.replace_document(current_space)

    return {}