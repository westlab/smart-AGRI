import requests
import json
headers = {'X-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBY2Nlc3NUb2tlbklkIjoiMzIwM2I5NDgtZDg0YS00NmE5LWIxNzItYjVhYzA3YzMyZTk2IiwiaXNzIjoiaHR0cHM6Ly9hcGkud2FncmkubmV0IiwiYXVkIjoiaHR0cHM6Ly9hcGkud2FncmkubmV0IiwiZXhwIjoxNjMxNjI5MDk2LCJuYmYiOjE2MzE1ODU4OTZ9.J4cmVB7_foVfmFSflXpFDqXBGjrkQuEuB8DXBORdgR8'}
response = requests.get('https://api.wagri.net/API/Public/Weather/Forecast',headers=headers)
##print(response.status_code)    # HTTPのステータスコード取得
response.headers = {"Content-Type": "application/json; charset=utf-8"}
data = response.json()
##print (json.dumps(data, indent=4))    ##これは日本語文字化けする
print (response.text)   ##レスポンスを全てテキストで出力