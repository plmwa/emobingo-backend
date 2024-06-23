import requests
from uuid import uuid4
import base64

# エンドポイントURL
url = "http://localhost:7071/api/users"

# ヘッダー（必要に応じて追加）
headers={
    "Content-Type":"application/json"
}
# JSONペイロード
target_file1 ='C:/Users/murai genta/Documents/wakayama/class/emobingo/rest_function/test/images/smile.jpg'
target_file2 ='C:/Users/murai genta/Documents/wakayama/class/emobingo/rest_function/test/images/angry.jpg'
target_file3 ='C:/Users/murai genta/Documents/wakayama/class/emobingo/rest_function/test/images/cry.jpg'
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
    "id" : str(uuid4()),#photonのuserIDを入れる
    "name": "testuser1",
    "room_id":"1111",#ここはphotonのroomIDを入れる
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
