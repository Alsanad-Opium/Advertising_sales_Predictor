import requests 

url = "http://127.0.0.1:5000/predict_form"

response = requests.post(url, data={
    "tv": 57.5,
    "radio": 32.8,
    "newspaper": 23.5
})



print("Status Code:", response.status_code)
print("Raw Response:", response.text)
# print(response.json())s