# Load

import pandas as pd
from azure.storage.blob import BlobServiceClient,BlobClient,ContainerClient
import sys

#sys.path.insert(0, 'D:\lina_lau\C339_datafundamentals\data_analysis_project')

class Load:
    def __init__(self, name, dataset):
        self.dataset = dataset
        self.name = name

    def azure_push(self):
        dataset = self.dataset

        csv_data = dataset.to_csv(index=False)

        connection_string = "DefaultEndpointsProtocol=https;AccountName=linalaustorage;AccountKey=0Y6GK2rWT19KW+0wAoi+0g/Bsow1Ch42GRwSKPS4vwVXVmmIElivviIj/97JPh44S2XLfgXkeAN1+AStHwNn9g==;EndpointSuffix=core.windows.net"
        container_name = "testcontainer/testDirectory"
        blob_name = self.name
        print(f'Trying to store {blob_name} in {container_name}')

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        #blob_service_client.max_single_put_size = 20*1024*1024
        #blob_service_client.timeout = 14400
        container_Client = blob_service_client.get_container_client(container_name)
        blob_client = container_Client.get_blob_client(blob_name)
        blob_client.upload_blob(csv_data, 
                                blob_type="BlockBlob",
                                connection_timeout=600,
                                overwrite = True)

