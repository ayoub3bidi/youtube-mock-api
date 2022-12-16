import requests

BaseURL = "http://127.0.0.1:5000"

response = requests.get(BaseURL + "/hello")
print(response.json())