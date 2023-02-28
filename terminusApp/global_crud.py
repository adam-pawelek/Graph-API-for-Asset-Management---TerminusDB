from fastapi import HTTPException, status

from terminusApp.database import client





def get_all(type: str):
    matches = client.query_document({"@type": type})
    result = list(matches)
    return result


def get(type: str, id: str):
    matches = client.query_document({"@type": type, "@id": id})
    result = list(matches)
    if len(result) > 0:
        return result[0]
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Not Found")


def delete(type: str, id: str):
    if type not in id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Type != id")
    else:
        try:
            client.delete_document(id)
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Found")
    return {}






def add_to_list(main_id, add_id, type):
    try:
        space = client.get_document(main_id)
        room = client.get_document(add_id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")
    if add_id in space[type]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Room already in space")

    space[type].append(add_id)
    query = client.replace_document(space)
    return

def remove_from_list(main_id, remove_id, type):
    try:
        space = client.get_document(main_id)
        room = client.get_document(remove_id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")
    if remove_id not in space[type]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")

    space[type].remove(remove_id)
    query = client.replace_document(space)
    return


def change_attribute(main_id, change_id, type):
    try:
        current_space = client.get_document(main_id)
        room = client.get_document(change_id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")
    current_space[type] = change_id
    query = client.replace_document(current_space)

    return {}