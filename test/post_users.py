import requests
from uuid import uuid4
# エンドポイントURL
url = "http://localhost:7071/api/users"

# ヘッダー（必要に応じて追加）
headers = {
    "Content-Type": "application/json"
}

# JSONペイロード
payload = {
    "id" : str(uuid4()),#photonのuserIDを入れる
    "name": "testuser1",
    "room_id":"1111",#ここはphotonのroomIDを入れる
    "images": [
        {
            "url": "1画像のURL",
            "emotion":"egao"
        },
        {
            "url": "2画像のURL",
            "emotion":"egao"
        },
        {
            "url": "3画像のURL",
            "emotion":"egao"
        }
    ]
}

# POSTリクエストを送信
response = requests.post(url, json=payload, headers=headers)

# レスポンスのステータスコードと内容を出力
print("ステータスコード:", response.status_code)
print("レスポンス内容:", response)
