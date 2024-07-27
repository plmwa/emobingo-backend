import azure.functions as func
from logging import getLogger 
import logging
from azure.cosmos import CosmosClient
import json
from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient
import base64
import uuid
import json

logger = getLogger(__name__)


load_dotenv()


client = CosmosClient.from_connection_string(conn_str=os.getenv("COSMOS_CONNECTION_STRING")) 
database_name = "cosmicworks"

database = client.get_database_client(database_name)
container_Users = database.get_container_client("Users")
container_Rooms = database.get_container_client("Rooms")

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# コンテナ名
container_name = "images"

# コンテナクライアントの作成
container_client = blob_service_client.get_container_client(container_name)

def create_user(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Handling POST request')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON body",
            status_code=400
        )

    #jsonデータ取り出し
    user_id = req_body.get('id')
    if not user_id:
        return func.HttpResponse(
            "UserID is required",
            status_code=400
        )
    
    name = req_body.get('name')
    if not name:
        return func.HttpResponse(
            "Name is required",
            status_code=400
        )
    
    images = req_body.get('images')
    if not images:
        return func.HttpResponse(
            "images is required",
            status_code=400
        )
    
    room_id = req_body.get('room_id')
    if not room_id:
        return func.HttpResponse(
            "Room is required",
            status_code=400
        )

    # Process images
    images_data = []
    for image in images:
        image_data = base64.b64decode(image["image_base64"])
        images_data.append(image_data)

    image_urls = []
    for image in images_data:
        image_filename = str(uuid.uuid4()) + ".jpg"
        blob_client = container_client.get_blob_client(image_filename)

        # Convert image to bytes and upload to Blob Storage
        blob_client.upload_blob(image)

        # Store URL of the image
        image_url = blob_client.url
        image_urls.append(image_url)

    #jsonを入れかえたい
    for i, image in enumerate(images):
        image["url"] = image_urls[i]
        image.pop("image_base64")

    #データベースに追加
    new_user = {
        'id': user_id,
        'name': name,
        'images': images,
        "room_id":room_id
    }
    container_Users.create_item(body=new_user)

    return func.HttpResponse(
        json.dumps(new_user, default=str),
        mimetype="application/json",
        status_code=200
    )

def get_user(req: func.HttpRequest, user_id: str) -> func.HttpResponse:
    logging.info('Handling GET user request')
    query = f"SELECT * FROM c WHERE c.id = '{user_id}'"
    items = list(container_Users.query_items(query=query, enable_cross_partition_query=True))

    if not items:
        return func.HttpResponse("User not found", status_code=404)

    return func.HttpResponse(
        json.dumps(items[0], default=str),
        mimetype="application/json",
        status_code=200
    )

def delete_user(req: func.HttpRequest, user_id: str) -> func.HttpResponse:
    logging.info('Handling DELETE user request')
    query = f"SELECT * FROM c WHERE c.id = '{user_id}'"
    items = list(container_Users.query_items(query=query, enable_cross_partition_query=True))

    if not items:
        return func.HttpResponse("User not found", status_code=404)

    container_Users.delete_item(item=items[0],partition_key=items[0]["id"])

    return func.HttpResponse(
        json.dumps(items[0], default=str),
        mimetype="application/json",
        status_code=200
    )