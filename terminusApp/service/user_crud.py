from typing import Optional

from fastapi import HTTPException, status

import terminusApp.auth.utils
from terminusApp import  models, schema
from terminusApp.database import client


def get_noraml_user(id):
    user = client.get_document(id)
    return user



def get_user_by_email( email: str) -> Optional[dict]:
    # Define the WOQL query to search for a user by email
    matches = client.query_document({"@type": "User",
                                     "email": email})
    #matches = matches.__dict__
    #print(type(matches))
    #print(matches[0])
    #user = json.dumps(matches)
    #user_try =  json.loads(user[0], object_hook = models.User)
    result = list(matches)
    my_dict= result[0]

    user = models.User(name=my_dict["name"], surname = my_dict["surname"], email= my_dict["email"], password = my_dict["password"], role = my_dict["role"])


    print( user.email)

    return user





def create_normal_user(user_schema : schema.UserSchema):
    my_exception = 0
    try:
        matches = client.query_document({"@type": "User","email": user_schema.email})
        result = list(matches)
        print(result)
        if len(result) > 0:
            my_exception = 1
    except:
        pass

    if my_exception ==1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email in database")

    hashed_password = terminusApp.auth.utils.get_password_hash(user_schema.password)
    user = models.User(name=user_schema.name, surname = user_schema.surname, email= user_schema.email, password = hashed_password, role ="user")
    client.insert_document([user])
    return {"message": f"Hello {user_schema}"}


def create_admin_user(user_schema : schema.UserSchema):
    my_exception = 0
    try:
        matches = client.query_document({"@type": "User","email": user_schema.email})
        result = list(matches)
        print(result)
        if len(result) > 0:
            my_exception = 1
    except:
        pass

    if my_exception ==1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email in database")

    
    hashed_password = terminusApp.auth.utils.get_password_hash(user_schema.password)
    user = models.User(name=user_schema.name, surname = user_schema.surname, email= user_schema.email, password = hashed_password, role ="admin")
    client.insert_document([user])
    return {"message": f"Hello {user_schema}"}



def delete_noraml_user(id):
    client.delete_document(id)
    return (list(client.get_all_documents()))




def update_normal_user(new_user : schema.UserSchema, id): #### admin
    current_user = client.get_document(id)
    current_user["name"] = new_user.name
    current_user["surname"] = new_user.surname
    current_user["email"] = new_user.email
    current_user["password"] = new_user.password
    query = client.replace_document(current_user)

    return {}