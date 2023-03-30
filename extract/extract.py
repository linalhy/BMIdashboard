import pandas as pd
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import io
import os
import pyodbc   

class Extract:
    #CONTAINER_NAME = input("Enter the container name: ")
    #CONNECTION_STRING = input("Enter the connection string for your container: ")
    print("Extract module imported succesfully.")
    CONTAINER_NAME = "testcontainer"
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=linalaustorage;AccountKey=0Y6GK2rWT19KW+0wAoi+0g/Bsow1Ch42GRwSKPS4vwVXVmmIElivviIj/97JPh44S2XLfgXkeAN1+AStHwNn9g==;EndpointSuffix=core.windows.net"

    def __init__(self):
        pass

    def getCSV(self, path): 
        container_name = Extract.CONTAINER_NAME

        blob_service_client = BlobServiceClient.from_connection_string(Extract.CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container_name, path)

        blob_data = blob_client.download_blob()
        data = pd.read_csv(io.StringIO(blob_data.content_as_text()))
        #print(data.head(5))
        print(f"{data} extracted succesfully!")
        return data
        
    def getJSON(self):
        pass










