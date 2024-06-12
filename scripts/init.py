#!/usr/bin/python3

import requests

url = "https://dvf-api.data.gouv.fr/dvf/csv/?section=31555822AB"
response = requests.get(url)

with open("data/dvf.csv", "wb") as f:
    f.write(response.content)
