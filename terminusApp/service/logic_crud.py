from terminusApp import models, schema
from terminusApp.database import client


def get_logic(id):
    logic = client.get_document(id)
    return logic

######### jak cos jest glopie ale dziala to znaczy ze nie jest glopie

def create_logic(logic_schema : schema.LogicSchema, space_id: str):
    person = models.Person(name="", surname="")
    space = models.Space(label="", type="", capacity=0, room=[],
                         reference=person, equipment=[])
    logic = models.Logic(label = logic_schema.label, type = logic_schema.type, use_case = space)

    logic_id = client.insert_document(logic)

    schema_id = logic_id[1]
    person_id = logic_id[2]
    logic_id = logic_id[0]
    print(logic_id)
    logic = client.get_document(logic_id)

    logic["use_case"] = space_id
    client.replace_document(logic)
    client.delete_document(schema_id)
    client.delete_document(person_id)
    return {}




def delete_logic(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))




def update_logic(new_logic :schema.LogicSchema, id):
    current_logic = client.get_document(id)
    current_logic["label"] = new_logic.label
    current_logic["type"] = new_logic.type
    query = client.replace_document(current_logic)

    return {}

