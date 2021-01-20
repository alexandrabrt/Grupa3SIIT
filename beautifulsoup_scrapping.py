import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.emag.ro/search/masti-chirurgicale-medicale/stoc/filter/numar-bucati-set-f8165,peste-20-v27424/masti/c?ref=lst_leftbar_8165_27424")
# print(r.text)
link = BeautifulSoup(r.text, 'html.parser')
# print(link)
title = link.find_all('div', attrs={'class': 'js-products-container card-collection list-view-updated show-me-a-grid'})
data_values = {'produs': [], 'pret': [], 'header': ['produs', 'pret']}
# <p class="product-new-price">29<sup>99</sup> <span>Lei</span></p>>
counter = 0
for x in title:
    for href in x.find_all('a', attrs={'class': 'thumbnail-wrapper js-product-url'}):
        print(href['href'])
        access = requests.get(href['href'])
        link_access = BeautifulSoup(access.text, 'html.parser')
        table = link_access.find_all('table', attrs={'class': 'table table-striped product-page-specifications'})
        all_values = None
        for item_title in table:
            all_values = item_title.find_all('td')
        keys = all_values[0::2]
        values = all_values[1::2]
        for j in keys:
            data_values['header'].append(j.get_text())
        for item in data_values['header']:
            data_values[item] = []

        for i in range(len(keys)):
            data_values[keys[i].get_text()].append(values[i].get_text())
        break
    for item in x.find_all('a', attrs={'class': 'product-title js-product-url'}):
        data_values['produs'].append(str(item.get_text()).lstrip().rstrip())
    for pret in x.find_all('p', attrs={'class': 'product-new-price'}):
        all_price = pret.get_text()
        decimal = pret.find('sup').get_text()
        pret_final = f"{all_price[:len(decimal) + 1]}.{decimal} {pret.find('span').get_text().upper()}"
        print(pret_final)
        data_values['pret'].append(pret_final)


print(data_values)

df = pd.DataFrame(data_values, columns=data_values['header'])
df.to_excel('/Users/alexandra/PycharmProjects/Grupa/dateMastiEmag.xls', sheet_name='all_product')