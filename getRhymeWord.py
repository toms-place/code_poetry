from bs4 import BeautifulSoup
import requests
import random

elem = input("Want to rhyme?\n\n")

page_link = 'https://reime.woxikon.de/ger/' + elem + '.php'

page_response = requests.get(page_link, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

textContent = []
links = page_content.find_all('div', {"class": "rhymes-list-word"})
for rhymes in links:
    textContent.append(rhymes.select('a')[0].text.replace("{n}", "").replace("{f}", "").replace("{m}", "").strip())

print(random.choice(textContent))