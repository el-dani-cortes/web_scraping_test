#!/usr/bin/python
import requests
from bs4 import BeautifulSoup as soup

for page in range(1, 6):
    # Collect and parse for every page.
    url = 'https://www.falabella.com.co/falabella-co/category/cat1360967/Televisores?page=' + str(page)
    html = requests.get(url)
    bs = soup(html.text, 'html.parser')

    # Pull all div tag with a specific tag. A list of products container.
    containers = bs.find_all(class_="jsx-1585533350")

    # Pull and print for every product the brand, name and price.
    print()
    print("############### Page - {} ###############".format(page))
    print()
    for container in containers:
        brand = container.find('b')
        name = container.find('span').b
        price = container.find('div', class_="jsx-3342506598").span
        print("Marca: {}".format(brand.text.strip()))
        print("Nombre: {}".format(name.text.strip()))
        print("Precio: {}".format(price.text.strip()))
        print("--------------------------------")
