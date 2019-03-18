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
                #print("no Synonym found")
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
                        Reimwortliste.append(rhymes.select('a')[0].text.replace("{n}", "").replace("{nm}", "").replace("{f}", "").replace("{m}", "").strip())

                returnWord = random.choice(Reimwortliste)
        except IndexError:
                #print("no Rhyme found")
                pass

        return returnWord

def Konjugation(word, person="ich", zeit="Präsens", imperative=False, iForm=1):
        #print(person + " -->")
        returnWord = word
        try:
                page_link = 'https://verben.woxikon.de/verbformen/' + str(word) + '.php'
                page_response = requests.get(page_link, timeout=5)
                page_content = BeautifulSoup(page_response.content, "html.parser")
                if imperative != True:
                        table = page_content.find_all('table', {"class": "conjugations-table"})[1]
                        tds = table.select('td')
                        for i, td in enumerate(tds):
                                if (i%6 == 0) & (person == "ich"):
                                        returnWord = td.text.strip()
                                        #print(td.text.strip())
                                elif (i%6 == 1) & (person == "du"):
                                        returnWord = td.text.strip()
                                        #print(td.text.strip())
                                elif (i%6 == 2) & (person == "er/sie/es"):
                                        returnWord = td.text.strip()
                                        #print(td.text.strip())
                                elif (i%6 == 3) & (person == "wir"):
                                        returnWord = td.text.strip()
                                        #print(td.text.strip())
                                elif (i%6 == 4) & (person == "ihr"):
                                        returnWord = td.text.strip()
                                        #print(td.text.strip())
                                elif (i%6 == 5) & (person == "sie"):
                                        returnWord = td.text.strip()
                                        #print(td.text.strip())
                                if (i == 5) & (zeit == "Präsens") or (i == 11) & (zeit == "Präteritum") or (i == 17) & (zeit == "Futur I Indikativ") or (i == 23) & (zeit == "Futur I Konjunktiv II") or (i == 29) & (zeit == "Präsens Konjunktiv I") or (i == 35) & (zeit == "Präteritum Konjunktiv II") or (i == 41) & (zeit == "Perfekt Indikativ") or (i == 47) & (zeit == "Plusquamperfekt Indikativ") or (i == 53) & (zeit == "Futur II Indikativ") or (i == 59) & (zeit == "Futur II Konjunktiv II") or (i == 65) & (zeit == "Perfekt Konjunktiv I") or (i == 71) & (zeit == "Plusquamperfekt Konjunktiv II"):
                                        break
                elif imperative == True:
                        table = page_content.find_all('table', {"class": "conjugations-table"})[0]
                        tds = table.select('td')
                        for i, td in enumerate(tds):
                                if i == iForm:
                                        returnWord = td.text.strip()


        except IndexError:
                #print("no Konjugation found")
                pass

        return returnWord