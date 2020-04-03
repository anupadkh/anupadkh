# importing the requests library
import requests

# api-endpoint
URL = "http://localhost:8000/snip/create_relief"


# defining a params dict for the parameters to be sent to the API
PARAMS = {
    "id":2,
    "receiver":2,
    "submitter": 1,
    "receiver_name": "Shiva Chand",
    "office": 1,
    "receiver_address": "Shankarpokhari",
    "mobile": 9856070774,
    "father_name": "Nanda Chand",
    "grandfather_name": "Kulami Chand",
    "relief_details": "Bhag Sale"
}


# sending get request and saving the response as response object
r = requests.post(url=URL, params=PARAMS)

# extracting data in json format
data = r.content

print(data)
# extracting latitude, longitude and formatted address
# of the first matching location
