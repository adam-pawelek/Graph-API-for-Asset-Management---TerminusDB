import  schema
import  models
from database import client
from collections import namedtuple

import json
from types import SimpleNamespace
import json

def get_logic(id):
    logic = client.get_document(id)
    return logic



def create_logic(logic_schema :schema.LogicSchema, space_id: str):
    space = client.get_document(space_id)
    print(space)
    space = json.dumps(space)
    space_try =  json.loads(space, object_hook = models.Space)
   # space_model = models.Space()
   # for key in space:
   #     setattr(space_model, key, my_dict[key])

    logic = models.Logic(label = logic_schema.label, type = logic_schema.type,use_case = space_try )
    #print (logic.label)
    #logic_insert = {}
    #logic_insert = logic.__dict__
    #logic_insert["use_case"] = space
    #print(logic_insert)
    #client.insert_document(logic_insert)
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