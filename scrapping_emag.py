import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get(
    "https://www.emag.ro/cutie-50-masti-faciale-de-unica-folosinta-sigilate-3-straturi-albastru-d9q76mmbm/pd/D9Q76MMBM/?X-Search-Id=abea50172aa565b87e4d&X-Product-Id=58887472&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view")

link = BeautifulSoup(r.text, 'html.parser')
data_values = {'header': []}
title = link.find_all('table', attrs={'class': 'table table-striped product-page-specifications'})
all_values = None
for x in title:
    all_values = x.find_all('td')

keys = all_values[0::2]
values = all_values[1::2]

for j in keys:
    data_values['header'].append(j.get_text())

for item in data_values['header']:
    data_values[item] = []

for i in range(len(keys)):
    data_values[keys[i].get_text()].append(values[i].get_text())

print(data_values)
df = pd.DataFrame(data_values, columns=data_values['header'])
df.to_excel('/Users/alexandra/PycharmProjects/Grupa/dateMastiEmag.xls')
