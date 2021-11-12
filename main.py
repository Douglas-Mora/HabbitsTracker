# This is not the final file to be used, go to recording_runs.py

# ------- Required modules
import requests

pixela_user = "https://pixe.la/@douglas-mora"
USER_NAME = "douglas-mora"
# I created this Token when creating the user.
TOKEN = "QEWrqqwrSDqwgtgetrStwertrdgthyt"

# ------- Initial "params" and "post request" sent to create the "user" and "passwordd":
"""
Step 1: Create your user account:
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes", 
}
response = requests.post(url="https://pixe.la/v1/users",json=user_params)
print(response.text)
>>> {"message":"Success.","isSuccess": true}
"""
# ------- Step 2: Create a graph definition:

graph_config = {
    "id": "graph1",
    "name": "Running Tracker",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
requests.post()


"""



requests.post(url=graph_endpoint, json=graph_config, headers=headers)


#response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
"""
