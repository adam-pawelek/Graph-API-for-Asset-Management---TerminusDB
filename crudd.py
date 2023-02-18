'''
from database import client

import  schema
import  models


def list_all():
    return (list(client.get_all_documents()))




def say_hello(item :schema.ItemSchema):
    my_dog = models.Pet(name=item.name, species=item.species, age=item.age, weight=item.weight)
    client.insert_document([my_dog])
    return {"message": f"Hello {item}"}



 def root():
    sth = (list(client.get_all_documents()))
    print ("asdfasdf")
    doc_id = sth[0]["@id"]
    client.delete_document(doc_id)
    return (list(client.get_all_documents()))


    '''