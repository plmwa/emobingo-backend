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
    if not images:
        return func.HttpResponse(
            "Room is required",
            status_code=400
        )
    
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
        status_code=201
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