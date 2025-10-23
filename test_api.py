import requests

url = 'http://127.0.0.1:5000/analyze'
data = {'text': "I'm so happy with this tool, it's amazing!"}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
