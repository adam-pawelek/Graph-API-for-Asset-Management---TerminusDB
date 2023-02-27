from typing import List

import  schema
import  models
from database import client



def get_place(id):
    logic = client.get_document(id)
    return logic

######### jak cos jest glopie ale dziala to znaczy ze nie jest glopie

def create_place(place_schema :schema.PlaceSchema, spaces_id: List[str]):
    place = models.Place(label = place_schema.label, type = place_schema.type,location = [] )

    place_id = client.insert_document(place)

    place_id = place_id[0]
    print(place_id)
    print("asdfffffffffdsafsdafsdafsda")
    place = client.get_document(place_id)

    place["location"] = spaces_id
    client.replace_document(place)

    return {}




def delete_place(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))

