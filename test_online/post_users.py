import requests
from uuid import uuid4
import base64
from dotenv import load_dotenv
import os

# エンドポイントURL
url = " https://die-webapi.azurewebsites.net/api/users/"

load_dotenv()

function_key = os.getenv("AZURE_FUNCTIONS_KEY")

# ヘッダー（必要に応じて追加）
headers={
    "Content-Type":"application/json",
    'x-functions-key': function_key
}






# JSONペイロード
target_file1 ="C:/Users/towns/Documents/wakayama/class/DIE/emobingo-backend/test/images/smile.jpg"
target_file2 ="C:/Users/towns/Documents/wakayama/class/DIE/emobingo-backend/test/images/angry.jpg"
target_file3 ="C:/Users/towns/Documents/wakayama/class/DIE/emobingo-backend/test/images/cry.jpg"
#なんか相対パスだと動かない、なぜ？？？？？
with open(target_file1, 'rb') as f:
    data = f.read()
encode1 = base64.b64encode(data).decode('utf-8')

with open(target_file2, 'rb') as f:
    data = f.read()
encode2 = base64.b64encode(data).decode('utf-8')

with open(target_file3, 'rb') as f:
    data = f.read()
encode3 = base64.b64encode(data).decode('utf-8')


payload = {
    "id" : "デプロイテストpost_users",#photonのuserIDを入れる
    "name": "デプロイテスト",
    "room_id":"デプロイテスト",#ここはphotonのroomIDを入れる
    "images": [
        {
            "emotion":"smile",
            "image_base64":encode1
        },
        {
            "emotion":"angry",
            "image_base64":encode2
        },
        {
            "emotion":"cry",
            "image_base64":encode3
        }
    ]
}

# POSTリクエストを送信
response = requests.post(url, json=payload,headers=headers)

# レスポンスのステータスコードと内容を出力
print("ステータスコード:", response.status_code)
print("レスポンス内容:", response)
