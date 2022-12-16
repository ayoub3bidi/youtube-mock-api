import requests

BaseURL = "http://127.0.0.1:5000"

response = requests.get(BaseURL + "/hello/tim")
print(response.json())