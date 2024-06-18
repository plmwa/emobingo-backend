import requests

# ベースURL
base_url = "http://localhost:7071/api/users/"

# 取得したいユーザーのID
user_id = "1"  # 実際のユーザーIDに置き換える

# フルURLを作成
url = base_url + user_id

try:
    # GETリクエストを送信
    response = requests.get(url)

    # ステータスコードを確認
    if response.status_code == 200:
        # 成功した場合、レスポンスのJSONデータを取得
        data = response.json()
        print("取得したデータ:", data)
    else:
        # エラーを出力
        print(f"エラー: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    # ネットワークエラーや接続エラーの場合の処理
    print("リクエストが失敗しました:", e)
