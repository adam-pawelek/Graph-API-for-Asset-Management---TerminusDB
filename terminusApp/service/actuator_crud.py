from terminusApp import models, schema
from terminusApp.database import client



def get_actuator(id):
    actuator = client.get_document(id)
    return actuator


def create_actuator(actuatorSchema : schema.ActuatorSchema, space_id: str):

    person = models.Person(name="", surname="")
    space = models.Space(label="", type="", capacity=0, room=[],
                         reference=person, equipment=[])
    actuator = models.Actuator(label=actuatorSchema.label, type = actuatorSchema.type, hw_version = actuatorSchema.hw_version, installation_date = actuatorSchema.installation_date,
                               gateway_location=space, powered =[], network_link= [])

    actuator_id =client.insert_document([actuator])
    schema_id = actuator_id[1]
    person_id = actuator_id[2]
    actuator_id = actuator_id[0]

    actuator = client.get_document(actuator_id)
    actuator["gateway_location"] = space_id
    client.replace_document(actuator)
    client.delete_document(schema_id)
    client.delete_document(person_id)
    return actuator


def delete_actuator(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))


def update_actuator(new_actuator :schema.ActuatorSchemaUpdate, id):
    current_equipment = client.get_document(id)
    current_equipment["label"] = new_actuator.label
    current_equipment["type"] = new_actuator.type
    current_equipment["installation_date"] = new_actuator.installation_date
    current_equipment["hw_version"] = new_actuator.hw_version
    query = client.replace_document(current_equipment)
    return {}
    
