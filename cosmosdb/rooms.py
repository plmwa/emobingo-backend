from azure.cosmos import CosmosClient, PartitionKey
client = CosmosClient(
    url="https://localhost:8081",
    credential=(
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
    ),
)
database = client.create_database_if_not_exists(
    id="cosmicworks",
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