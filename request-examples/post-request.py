import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 587, "title": "Jagdish Tirumala", "completed": False}

response = requests.post(api_url, json=todo)
print("response.json() = ",response.json())
print("response.status code = ",response.status_code)
