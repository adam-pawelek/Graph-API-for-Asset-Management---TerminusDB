import  schema
import  models
from database import client



def get_noraml_user(id):
    user = client.get_document(id)
    return user




def create_normal_user(user_schema :schema.UserSchema):
    user = models.User(name=user_schema.name,surname = user_schema.surname, email= user_schema.email, password = user_schema.password, role = "user")
    client.insert_document([user])
    return {"message": f"Hello {user_schema}"}




def delete_noraml_user(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))




def update_normal_user(new_user :schema.UserSchema, id): #### admin
    current_user = client.get_document(id)
    current_user["name"] = new_user.name
    current_user["surname"] = new_user.surname
    current_user["email"] = new_user.email
    current_user["password"] = new_user.password
    query = client.replace_document(current_user)

    return {}