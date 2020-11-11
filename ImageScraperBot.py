from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import os
import requests

driver = webdriver.Chrome()

url = "https://www.pexels.com/search/waves/"

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")


image_tags = soup.find_all('img', {"class": "photo-item__img"})


print(image_tags)

# create directory for waves images
if not os.path.exists('waves'):
    os.makedirs('waves')

# move to new directory
os.chdir('waves')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('waves-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
