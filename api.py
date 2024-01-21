import requests


url = f"http://10.10.26.4:5000/api/ping/"

data_to_send = "10.179.36.10"
response = requests.post(url, json=data_to_send)

if response.status_code == 200:
    data = response.json()
    print(f"{data}")
else:
    print(f"Error: {response.status_code}")
    
