import requests
from dotenv import load_dotenv
import os

# ベースURL
url = " https://die-webapi.azurewebsites.net/api/rooms/"

# 送信したいデータ (例として、JSON形式でデータを定義)
data = {
    "room_id": "デプロイテスト"
}

load_dotenv()

function_key = os.getenv("AZURE_FUNCTIONS_KEY")

# ヘッダー（必要に応じて追加）
headers={
    'x-functions-key': function_key
}


try:
    # POSTリクエストを送信
    response = requests.post(url, json=data,headers=headers)

    # ステータスコードを確認
    if response.status_code == 201:
        # 成功した場合、レスポンスのJSONデータを取得
        response_data = response.json()
        print("POSTリクエストが成功しました:", response_data)
    else:
        # エラーを出力
        print(f"POSTリクエストが失敗しました: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    # ネットワークエラーや接続エラーの場合の処理
    print("リクエストが失敗しました:", e)
