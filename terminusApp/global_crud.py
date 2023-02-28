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