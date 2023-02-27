from typing import List

import  schema
import  models
from database import client



def get_place(id):
    logic = client.get_document(id)
    return logic

######### jak cos jest glopie ale dziala to znaczy ze nie jest glopie

def create_place(place_schema :schema.PlaceSchema, spaces_id: List[str]):
    person = models.Person(name="", surname="")
    space = models.Space(label="", type="", capacity=0, room=[],
                         reference=person, equipment=[])
    place = models.Place(label = place_schema.label, type = place_schema.type,location = [space] )

    place_id = client.insert_document(place)

    schema_id = place_id[1]
    person_id = place_id[2]
    place_id = place_id[0]
    print(place_id)
    print("asdfffffffffdsafsdafsdafsda")
    place = client.get_document(place_id)

    place["location"] = spaces_id
    client.replace_document(place)
    client.delete_document(schema_id)
    client.delete_document(person_id)

    return {}




def delete_place(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))

