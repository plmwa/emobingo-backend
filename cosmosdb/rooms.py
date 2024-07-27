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
    id="Rooms",
    partition_key=PartitionKey(
        path="/id",
    ),
)

item = {
    "id":"1234",
    "users": [
        {
            "user_id": "1",
            "name": "genta"
        },
        {
            "user_id": "2",
            "name": "koga"
        },
        {
            "user_id": "3",
            "name": "momoe"
        }
    ],
    "images": [
        {
            "user_id": "1",
            "url": "genta_1.jpg",
        },
        {
            "user_id": "2",
            "url": "koga_1.jpg",
        },
        {
            "user_id": "3",
            "url": "momoe_1.jpg",
        },
    ]
}

container.upsert_item(item)