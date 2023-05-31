import csv
import requests
from bs4 import BeautifulSoup

url = 'http://link.kg/catalog/1/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

notebook = soup.find_all('tr', class_='r2')

data = []

for x in notebook:
    td = x.find_all('td')
    
     title = td[1].text.strip()
     price_c = td[2].text.strip()
     price_d = td[3].text.strip()

     data.append([title, price_c, price_d])

with open('notebooks.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['titile', 'price_c', 'price_d'])
    writer.writerows(data)
