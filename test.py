import requests

url = "http://127.0.0.1:5000/display"
payload = {"text": "Hello VFD!"}
response = requests.post(url, json=payload)

print(response.json())


Invoke-RestMethod -Uri "http://127.0.0.1:5000/display" `
  -Method Post `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"text": "2000/=TSH"}'