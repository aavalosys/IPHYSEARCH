import requests


#############ping#######################
url = f"http://10.10.26.4:5000/api/ping/"

data_to_send = "10.179.36.10"
response = requests.post(url, json=data_to_send)

if response.status_code == 200:
    data = response.json()
    print(f"{data}")
else:
    print(f"Error: {response.status_code}")
    



#### get interface############
print ("get interface")

url = f"http://10.10.26.4:5000/api/getinterface/"

data_to_send = ["fy2023w48","10.123.45.6", "GigabitEthernet 0/2/24"]
response = requests.post(url, json=data_to_send)

if response.status_code == 200:
    data = response.json()
    print(f"{data}")
else:
    print(f"Error: {response.status_code}")
  


  
########### get ping vrf###########
print ("get vrf")
url = f"http://10.10.26.4:5000/api/getpingvrf/"

data_to_send = ["fy2023w48","10.179.28.33", "PS-Access" , "10.111.60.155"]
response = requests.post(url, json=data_to_send)

if response.status_code == 200:
    data = response.json()
    print(f"{data}")
else:
    print(f"Error: {response.status_code}")