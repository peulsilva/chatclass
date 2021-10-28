import requests

req = requests.get("http://www.boredapi.com/api/activity/")

print(req.json())
