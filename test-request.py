import requests

BaseURL = "http://127.0.0.1:5000"

# response = requests.put(BaseURL + "/video/1", {"name": "tim", "views": 100, "likes": 10})
# print(response.json())
# input()
response = requests.put(BaseURL + "/video/6")
print(response.json())