import  schema
import  models
from database import client
from collections import namedtuple
from types import SimpleNamespace
import json
from types import SimpleNamespace
import json

def get_logic(id):
    logic = client.get_document(id)
    return logic

######### jak cos jest glopie ale dziala to znaczy ze nie jest glopie

def create_logic(logic_schema :schema.LogicSchema, space_id: str):
    space_get = client.get_document(space_id)
    #print(space)
    #space = json.dumps(space)

    person = models.Person(name="", surname="")

    space = models.Space(label="", type="", capacity=0, room=[],
                         reference=person, equipment=[])
    logic = models.Logic(label = logic_schema.label, type = logic_schema.type,use_case = space )

    logic_id = client.insert_document(logic)

    logic_id = logic_id[0][19:]
    logic = client.get_document(logic_id)

    print ()
    logic["use_case"] = space_get
    query = client.replace_document(logic)


    return {}




def delete_logic(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))



'''
def update_logic(new_logic :schema.LogicSchema, id):
    current_logic = client.get_document(id)
    current_logic["name"] = new_person.name
    current_person["surname"] = new_person.surname
    query = client.replace_document(current_person)

    return {}

'''