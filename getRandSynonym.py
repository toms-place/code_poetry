import requests
import random
import json

def getRandSynonym(word):
        url = 'https://www.openthesaurus.de/synonyme/search?q=' + word + '&format=application/json'
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.get(url, headers=headers)
        data = json.loads(r.content)['synsets']

        print()

        termsList = []

        for terms in data:
                for term in terms['terms']:
                        termsList.append(term['term'])

        return(random.choice(termsList))

print(getRandSynonym(input("WORD!\n\n")))