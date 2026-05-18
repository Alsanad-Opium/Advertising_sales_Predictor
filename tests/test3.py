import requests 
import numpy as np
url = "http://127.0.0.1:5000/predict"


data = {
    'features':[[133393,46,777778]]
}

response = requests.post(url,json = data)

print(response.status_code)
print(response.text)