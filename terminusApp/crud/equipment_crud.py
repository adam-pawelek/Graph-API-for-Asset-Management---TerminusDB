from terminusApp import models, schema
from terminusApp.database import client



def get_equipment(id):
    equipment = client.get_document(id)
    return equipment



def create_equipment(equipmentSchema : schema.EquipmentSchema):
    equipment = models.Equipment(label=equipmentSchema.label, type = equipmentSchema.type, ports_numer = equipmentSchema.ports_numer, capacity = equipmentSchema.capacity)
    client.insert_document([equipment])
    return equipment




def delete_equipment(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))




def update_equipment(new_equipment : schema.EquipmentSchema, id):
    current_equipment = client.get_document(id)
    current_equipment["label"] = new_equipment.label
    current_equipment["type"] = new_equipment.type
    current_equipment["ports_numer"] = new_equipment.ports_numer
    current_equipment["capacity"] = new_equipment.capacity
    query = client.replace_document(current_equipment)

    return {}