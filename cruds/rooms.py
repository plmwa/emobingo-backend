import azure.functions as func
from logging import getLogger 
import logging
from azure.cosmos import CosmosClient

import json

logger = getLogger(__name__)

client = CosmosClient(
    url="https://localhost:8081",
    credential=(
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
    ),
)

database_name = "cosmicworks"

database = client.get_database_client(database_name)
container_Users = database.get_container_client("Users")
container_Rooms = database.get_container_client("Rooms")

def list_room_images(req: func.HttpRequest,room_id: str) -> func.HttpResponse:
    logging.info('Handling GET request')
    query = f"SELECT * FROM c WHERE c.id = '{room_id}'"
    items = list(container_Rooms.query_items(query=query, enable_cross_partition_query=True))

    if not items:
        return func.HttpResponse("Rooms not found", status_code=404)

    return func.HttpResponse(
        json.dumps(items[0], default=str),
        mimetype="application/json",
        status_code=200
    )

def create_room_images(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Handling POST request')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON body",
            status_code=400
        )

    #jsonデータ取り出し
    room_id = req_body.get('room_id')
    if not room_id:
        return func.HttpResponse(
            "Room is required",
            status_code=400
        )
    
    #Userコンテナからroom_idが一致するものを追加
    query = f"SELECT * FROM c WHERE c.room_id = '{room_id}'"
    items = list(container_Users.query_items(query=query, enable_cross_partition_query=True))
    
    if not items:
        return func.HttpResponse("UserコンテナにそのRoomは not found", status_code=404)
    
    # items から "user_id" と "name" のみを抽出したリストを作成する
    user_items = [{"user_id": item["id"], "name": item["name"]} for item in items]
    image_items = [item["images"] for item in items]

    new_room = {
        'id': room_id,
        'users': user_items,
        'images':image_items 
    }

    container_Rooms.create_item(body=new_room)

    return func.HttpResponse(
        json.dumps(new_room, default=str),
        mimetype="application/json",
        status_code=201
    )