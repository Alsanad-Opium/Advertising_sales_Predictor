import requests 

url = "http://127.0.0.1:5000/predict"

data = {
    "features":[[57.5,32.8,23.5]]
}

response = requests.post(url,json=data)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)
# print(response.json())