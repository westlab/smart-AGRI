import requests
import json
import pandas as pd
from pandas.io.json import json_normalize


headers = {'Content-Type': 'application/x-www-form-urlencoded'}
body = {'grant_type':'client_credentials','client_id':'a04d9a5c-fb87-4c1b-91ea-4edce22c1592','client_secret':'210oumn=ie'}
response = requests.post('https://api.wagri.net/Token',headers=headers,data=body)
response.headers = {"Content-Type": "application/json; charset=utf-8"}
data = response.json()
access_token = data["access_token"]
headers = {'X-Authorization': access_token}
response = requests.get('https://api.wagri.net/API/Public/Weather/Forecast',headers=headers)
print(response.status_code)    # HTTPのステータスコード取得
response.headers = {"Content-Type": "application/json; charset=utf-8"}
data = response.json()
print(data)
##data = json.dumps(data, indent=4) ##これは日本語文字化けする
##print (response.text[:300])   ##レスポンスを全てテキストで出力