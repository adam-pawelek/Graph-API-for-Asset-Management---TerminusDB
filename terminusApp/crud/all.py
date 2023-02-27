from terminusApp.database import client


def list_all():
    return (list(client.get_all_documents()))