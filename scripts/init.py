#!/usr/bin/env python3

import requests
import csv

response = requests.get("https://dvf-api.data.gouv.fr/dvf/csv/?section=31555822AB")

rows = response.content.decode('utf-8').split('\n')
first_row = rows[0]
rows = [row for row in rows if row != first_row]
rows.insert(0, first_row)

rows = [row.split(',') for row in rows]

with open('data/dvf.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
