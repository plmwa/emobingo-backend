import azure.functions as func
from logging import getLogger 
import logging
from azure.cosmos import CosmosClient
import json
import uuid
from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient
import os

load_dotenv()
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# コンテナ名
container_name = "images"

# コンテナクライアントの作成
container_client = blob_service_client.get_container_client(container_name)

images_data = [
    'C:/Users/murai genta/Documents/wakayama/class/emobingo/rest_function/test/images/smile.jpg',
    'C:/Users/murai genta/Documents/wakayama/class/emobingo/rest_function/test/images/angry.jpg',
    'C:/Users/murai genta/Documents/wakayama/class/emobingo/rest_function/test/images/cry.jpg'
]
image_path=[
    'smile.jpg',
    'angry.jpg',
    'cry.jpg'
]

image_urls = []
for image in images_data:
    blob_client = container_client.get_blob_client(image_path[images_data.index(image)])

    # Convert image to bytes and upload to Blob Storage
    with open(image, 'rb') as image:
        image_bytes = image.read()
    blob_client.upload_blob(image_bytes)

    # Store URL of the image
    image_url = blob_client.url
    image_urls.append(image_url)
print(image_urls)