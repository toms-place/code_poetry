from bs4 import BeautifulSoup
import requests
import random
import json

def Synonym(word):
        returnWord = word
        try:
                url = 'https://www.openthesaurus.de/synonyme/search?q=' + word + '&format=application/json'
                headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
                r = requests.get(url, headers=headers)
                data = json.loads(r.content)['synsets']
                Synonymliste = []
                for terms in data:
                        for term in terms['terms']:
                                Synonymliste.append(term['term'])
                returnWord = random.choice(Synonymliste)
        except IndexError:
                pass
        except json.decoder.JSONDecodeError:
                pass

        return returnWord

def Rhyme(word):
        returnWord = word
        try:
                page_link = 'https://reime.woxikon.de/ger/' + str(word) + '.php'
                page_response = requests.get(page_link, timeout=5)
                page_content = BeautifulSoup(page_response.content, "html.parser")
                Reimwortliste = []
                links = page_content.find_all('div', {"class": "rhymes-list-word"})

                for rhymes in links:
                        Reimwortliste.append(rhymes.select('a')[0].text.replace("{n}", "").replace("{f}", "").replace("{m}", "").strip())

                returnWord = random.choice(Reimwortliste)
        except IndexError:
                pass

        return returnWord