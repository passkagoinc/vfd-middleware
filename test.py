import requests

url = "http://127.0.0.1:5000/display"
payload = {"text": "Hello VFD!"}
response = requests.post(url, json=payload)

print(response.json())
