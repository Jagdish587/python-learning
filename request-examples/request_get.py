import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print("response.json() = ",response.json())
print("response.status code = ",response.status_code)
print("response.headers = ",response.headers["Content-Type"])