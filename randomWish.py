from bs4 import BeautifulSoup
import requests
import random

page_link = 'http://sprueche-wuensche.de/geburtstagswuensche/'

page_response = requests.get(page_link, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

textContent = []
wishes = page_content.find_all('p', {"class": "indent"})
for wish in wishes:
    textContent.append(wish.text)

print(random.choice(textContent))