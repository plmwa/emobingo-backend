import azure.functions as func
import cruds.users
import cruds.rooms

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
    
@app.route(route="users", methods=["POST"])
async def create_users(req: func.HttpRequest) -> func.HttpResponse:
    return cruds.users.create_user(req)


@app.route(route="users/{user_id}", methods=["GET"])
async def get_users(req: func.HttpRequest) -> func.HttpResponse:
    user_id = req.route_params.get('user_id')
    return cruds.users.get_user(req,user_id)
    
@app.route(route="rooms", methods=["POST"])
async def create_rooms(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "POST":
        return cruds.rooms.create_room_images(req)

@app.route(route="rooms/{room_id}", methods=["GET"])
async def get_rooms(req: func.HttpRequest) -> func.HttpResponse:
    room_id = req.route_params.get('room_id')
    if req.method == "GET":
        return cruds.rooms.list_room_images(req,room_id)
    