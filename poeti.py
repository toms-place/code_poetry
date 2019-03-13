from bs4 import BeautifulSoup
import requests
import random
import json

class Poeti:
    def __init__(self, name):
        self.name = name

    def getSynonym(self, word):
        url = 'https://www.openthesaurus.de/synonyme/search?q=' + word + '&format=application/json'
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.get(url, headers=headers)
        data = json.loads(r.content)['synsets']
        termsList = []
        for terms in data:
                for term in terms['terms']:
                        termsList.append(term['term'])
        return(random.choice(termsList))
    
    def getRhymeWord(self, word):
        page_link = 'https://reime.woxikon.de/ger/' + word + '.php'
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        textContent = []
        links = page_content.find_all('div', {"class": "rhymes-list-word"})
        for rhymes in links:
            textContent.append(rhymes.select('a')[0].text.replace("{n}", "").replace("{f}", "").replace("{m}", "").strip())
        return(random.choice(textContent))

    def saySomething(self, word):
        print(self.getSynonym(word))

    def antiReimABAB(self, words):
        for word in words:
            print("Wort: " + word)
            print("Synonym: " + self.getSynonym(word))
            print("Reim: " + self.getRhymeWord(word))

def main():
    poeti = Poeti("poeti")
    poeti.antiReimABAB(["weinen", "fließen", "scheinen", "sprießen"])

main()