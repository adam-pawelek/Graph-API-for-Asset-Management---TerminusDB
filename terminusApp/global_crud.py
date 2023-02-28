from terminusApp.database import client





def get_all(type: str):
    matches = client.query_document({"@type": type})
    result = list(matches)
    return result


def get(type: str, id: str):
    matches = client.query_document({"@type": type, "@id": id})
    result = list(matches)
    return result[0]


def delete(type: str, id: str):
    if type not in id:
        pass
    else:
        client.delete_document(id)
    return {}