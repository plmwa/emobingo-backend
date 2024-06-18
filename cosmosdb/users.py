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