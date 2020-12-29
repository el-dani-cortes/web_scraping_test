#!/usr/bin/python
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

#Options for chrome
coptions = webdriver.ChromeOptions()
#coptions.add_argument('--ignore-certificate-errors')
coptions.add_argument('--incognito')
#coptions.add_argument('--headless')

#Function to render full page content
def render_page(url):
    driver = webdriver.Chrome(chrome_options=coptions)
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    # driver.quit()
    return r

#Web scrapping
for page in range(1,6):
    url = 'https://www.falabella.com.co/falabella-co/category/cat1360967/Televisores?page=' + \
        str(page)
    render = render_page(url)
    soup = bs(render, "html.parser")
    containers = soup.find_all(class_="jsx-1585533350")
    # print(soup.prettify())
    for container in containers:
        brand = container.find('b')
        name = container.find('span').b
        price = container.find('div', class_="jsx-3342506598").span
        print("--------------------------------")
        print("Marca: {}".format(brand.text.strip()))
        print("Nombre: {}".format(name.text.strip()))
        print("Precio: {}".format(price.text.strip()))
    print(len(containers))
