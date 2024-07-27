from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv
import os

load_dotenv()
client = CosmosClient(
    url=os.getenv("COSMOS_CONNECTION_URL"),
    credential=os.getenv("COSMOS_CONNECTION_KEY")
)
database = client.create_database_if_not_exists(
    id="Emobingo",
    offer_throughput=400,
)

container = database.create_container_if_not_exists(
    id="Users",
    partition_key=PartitionKey(
        path="/id",
    ),
)

item = {
    "id":"1",
    "name":"genta",
    "room_id":"1123",
    "images":[
        {
            "emotion":"egao",
            "url":"genta_1.jpg",
    
        },
        {
            "emotion":"egao",
            "url":"genta_2.jpg",
        }
    ]
}

container.upsert_item(item)

item = {
    "id":"1",
    "name":"genta",
    "room_id":"1234",
    "images":[
        {
            "emotion":"egao",
            "url":"genta_1.jpg",
    
        },
        {
            "emotion":"egao",
            "url":"genta_2.jpg",
        }
    ]
}

container.upsert_item(item)

item = {
    "id":"2",
    "name":"koga",
    "room_id":"1234",
    "images":[
        {
            "emotion":"egao",
            "url":"koga_1.jpg",
    
        },
        {
            "emotion":"egao",
            "url":"koga_2.jpg",
        }
    ]
}

container.upsert_item(item)

item = {
    "id":"3",
    "name":"momoe",
    "room_id":"1234",
    "images":[
        {
            "emotion":"egao",
            "url":"momoe_1.jpg",
    
        },
        {
            "emotion":"egao",
            "url":"momoe_2.jpg",
        }
    ]
}

container.upsert_item(item)