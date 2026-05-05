import requests
import pandas as pd

# Obtener token
token_response = requests.post(
    "https://restapi-masair.apm.ch/prod-restapi/oauth/token",
    data={"grant_type": "client_credentials"},
    auth=("M7API", "12345")
)

access_token = token_response.json()["access_token"]

headers = {
    "accept": "application/hal+json;charset=UTF-8",
    "Authorization": f"Bearer {access_token}"
}

# Endpoint correcto
r = requests.get(
    "https://restapi-masair.apm.ch/prod-restapi/api/dictionaries/airport-equipments/values",
    headers=headers
)

data = r.json()

if "_embedded" in data:
    dataset = pd.json_normalize(data["_embedded"]["contactDtoList"])
else:
    dataset = pd.json_normalize(data)

print(dataset)
