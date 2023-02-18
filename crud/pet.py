

import  schema

import  models
from database import client



def get_pet(id):
    pet = client.get_document(id)
    return pet



def create_pet(item :schema.PetSchema):
    my_dog = models.Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    client.insert_document([my_dog])
    return {"message": f"Hello {item}"}




def delete_pet():
    sth = (list(client.get_all_documents()))
    print ("asdfasdf")
    doc_id = sth[0]["@id"]
    client.delete_document(doc_id)
    return (list(client.get_all_documents()))




def update_pet():
    sth = (list(client.get_all_documents()))
    print ("asdfasdf")
    doc_id = sth[0]["@id"]
    cos = client.get_document(doc_id)
    my_dog = {}
    cos["name"] = "update"
    cos["species"] = "ll"
    cos["age"] = 1
    cos["weight"] =12
    print(my_dog)

    query = client.replace_document(cos)

    return {}
