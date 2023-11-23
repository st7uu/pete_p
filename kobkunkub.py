
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kobkubkub:Pp#pw.7555@cluster0.im6ch57.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


mydb = client.get_database('event')
records = mydb.kobkubkub

def get_img():
    for i in records.find({},{'_id': 0}):
        return i