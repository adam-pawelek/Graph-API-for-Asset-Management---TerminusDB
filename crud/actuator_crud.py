


import  schema
import  models
from database import client



def get_actuator(id):
    actuator = client.get_document(id)
    return actuator



def create_actuator(actuatorSchema :schema.ActuatorSchema,  space_id: str):

    person = models.Person(name="", surname="")
    space = models.Space(label="", type="", capacity=0, room=[],
                         reference=person, equipment=[])

    actuator = models.Actuator(label=actuatorSchema.label,type = actuatorSchema.type,hw_version = actuatorSchema.hw_version,installation_date = actuatorSchema.installation_date,
                                 gateway_location=space  , powered =[]  , network_link= [])

    actuator_id =client.insert_document([actuator])


    schema_id = actuator_id[1]
    person_id = actuator_id[2]
    actuator_id = actuator_id[0]
    print(actuator_id)
    actuator = client.get_document(actuator_id)

    actuator["gateway_location"] = space_id
    client.replace_document(actuator)
    client.delete_document(schema_id)
    client.delete_document(person_id)

    return actuator




def delete_actuator(id):
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