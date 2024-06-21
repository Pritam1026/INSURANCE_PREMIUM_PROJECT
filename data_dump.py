from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://singhpritam983:VncOjIRbC8kUNzAV@cluster0.pzxsxnq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
#client creation

DATA_FILE_PATH="insurance.csv" #Path of the data
DATABASE_NAME="INSURANCE" 
COLLECTION_NAME="INSURANCE_PROJECT"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH) #Reading the data
    print(f"There are {df.shape} rows and columns in the dataset.")

    df.reset_index(drop=True,inplace=True) #Resetting the index so that uneven indexes are present. 
    #This step is optional if the index are simply serial numbers.
    json_records=list(json.loads(df.T.to_json()).values()) #Converting the data to json records.

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records) #Loading data to mongodb

    
