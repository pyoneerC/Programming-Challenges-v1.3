import requests

url = 'https://www.example.com'
count = 1000

for i in range(count):
    response = requests.get(url)
    print(f'Response {i + 1}: {response.status_code}')