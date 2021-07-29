import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print("response.json() = ",response.json())
print("response.status code = ",response.status_code)

todo = {"userId": 1, "title": "Jagdish car", "completed": True}
response = requests.put(api_url, json=todo)

print("response.json() = ",response.json())
print("response.status code = ",response.status_code)

