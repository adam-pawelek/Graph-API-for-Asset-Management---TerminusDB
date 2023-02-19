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




def delete_pet(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))




def update_pet(new_pet :schema.PetSchema, id):
    current_pet = client.get_document(id)
    my_dog = {}
    current_pet["name"] = new_pet.name
    current_pet["species"] = new_pet.species
    current_pet["age"] = new_pet.age
    current_pet["weight"] = new_pet.weight

    query = client.replace_document(current_pet)

    return {}
