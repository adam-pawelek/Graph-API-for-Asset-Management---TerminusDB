from terminusdb_client import Client, WOQLClient, WOQLSchema

client = WOQLClient("http://127.0.0.1:6363/")
client.connect()