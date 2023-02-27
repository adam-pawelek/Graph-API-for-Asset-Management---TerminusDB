from terminusApp import models, schema
from terminusApp.database import client



def get_sensor(id):
    actuator = client.get_document(id)
    return actuator



def create_sensor(sensorSchema : schema.SensorSchema, space_id: str):
    person = models.Person(name="", surname="")
    space = models.Space(label="", type="", capacity=0, room=[],
                         reference=person, equipment=[])

    sensor = models.Sensor(label=sensorSchema.label, type=sensorSchema.type, fw_version = sensorSchema.fw_version,
                           hw_version=sensorSchema.hw_version, installation_date=sensorSchema.installation_date,
                           sensor_location=space)

    actuator_id = client.insert_document([sensor])

    schema_id = actuator_id[1]
    person_id = actuator_id[2]
    actuator_id = actuator_id[0]
    print(actuator_id)
    actuator = client.get_document(actuator_id)

    actuator["sensor_location"] = space_id
    client.replace_document(actuator)
    client.delete_document(schema_id)
    client.delete_document(person_id)

    return actuator


def delete_sensor(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))


'''
def update_equipment(new_equipment :schema.EquipmentSchema, id):
    current_equipment = client.get_document(id)
    current_equipment["label"] = new_equipment.label
    current_equipment["type"] = new_equipment.type
    current_equipment["ports_numer"] = new_equipment.ports_numer
    current_equipment["capacity"] = new_equipment.capacity
    query = client.replace_document(current_equipment)

    return {}

'''