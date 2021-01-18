import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.emag.ro/search/masti/p2")
# print(r.text)
link = BeautifulSoup(r.text, 'html.parser')
# print(link)
title = link.find_all('div', attrs={'class': 'js-products-container card-collection list-view-updated show-me-a-grid'})
data_values = {'status': [], 'produs': [], 'pret': [], 'livrat_de': []}
# <p class="product-new-price">29<sup>99</sup> <span>Lei</span></p>>
counter = 0
for x in title:
    for status in x.find_all('p', attrs={'class': 'product-stock-status'}):
        data_values['status'].append(status.get_text())
    for item in x.find_all('a', attrs={'class': 'product-title js-product-url'}):
        data_values['produs'].append(str(item.get_text()).lstrip().rstrip())
    for pret in x.find_all('p', attrs={'class': 'product-new-price'}):
        all_price = pret.get_text()
        decimal = pret.find('sup').get_text()
        pret_final = f"{all_price[:len(decimal) + 1]}.{decimal} {pret.find('span').get_text().upper()}"
        data_values['pret'].append(pret_final)
    # for livrare in x.find_all('p', attrs={'class': 'product-vendor text-truncate'}):
    #     data_values['livrat_de'].append(f"{livrare.find('span').get_text()} {livrare.find('a').get_text()}")
# print(data_values)

df = pd.DataFrame(data_values, columns=['status', 'produs', 'pret', 'livrat_de'])
df.to_excel('/Users/alexandra/PycharmProjects/Grupa3SIIT/dateMastiEmag.xls', sheet_name='all_product')