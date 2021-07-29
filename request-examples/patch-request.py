import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print("response.json() = ",response.json())
print("response.status code = ",response.status_code)

new_title = {'title': 'Jagdish Tirumala'}
response = requests.patch(api_url,json = new_title)

print("response.json() = ",response.json())
print("response.status code = ",response.status_code)


