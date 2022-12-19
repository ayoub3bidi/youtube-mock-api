import requests

BaseURL = "http://127.0.0.1:5000"

# data = [
#     {"name": "tim", "views": 11120, "likes": 10},
#     {"name": "bill", "views": 8790, "likes": 780},
#     {"name": "tommy", "views": 9800, "likes": 19510}
# ]

# for i in range(len(data)):
#     response = requests.put(BaseURL + "/video/" + str(i), data[i])
#     print(response.json())

# input()
response = requests.patch(BaseURL + "/video/2", {})
print(response.json())