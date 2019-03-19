import csv
import yaml
from bs4 import BeautifulSoup
import requests
import random


#returns an array of lines with 
def fromTXT(filepath):
        para = []

        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                para.append(line.strip())
                line = fp.readline()
                cnt += 1

        lines = []
        for line in para:
            if line != "":
                words = line.split(" ")
                lines.append(words)
            else:
                lines.append("ABSATZ")

        return(lines)

def fromCSV(filepath):
    lines = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            lines.append(row)
    return lines

def fromYAML(filepath):
    lines = []
    with open(filepath, 'r') as stream:
        try:
            data = yaml.load(stream, Loader=yaml.FullLoader)
            for word in data:
                lines.append(word)
        except yaml.YAMLError as exc:
            print(exc)
    return lines

def fromSongtexte(word):
        para = []
        try:
                page_link = 'https://www.lyrix.at/lyrics-search/?sartist=&stitle=' + str(word) + '&stext=&lgroups_text=true&lgroups_translation=true&ssubmit=Suchen%21#results'
                page_response = requests.get(page_link, timeout=5)
                page_content = BeautifulSoup(page_response.content, "html.parser")

                links = page_content.find_all('section', {"class": "result-part"})

                page_link_songtext = 'https://www.lyrix.at' + random.choice(links).select('a')[0]['href']
                page_response_songtext = requests.get(page_link_songtext, timeout=5)
                page_content_songtext = BeautifulSoup(page_response_songtext.content, "html.parser")


                text = page_content_songtext.find_all('div', {"id": "stextDIV"})[0]
                for line in text:
                    if line.find('<br>'):
                        para.append(line.strip())
                
                print("Künstler: " + page_content_songtext.find_all('a', {"class": "artist"})[0].text)
                print("Originaltitel: " + page_content_songtext.find_all('span', {"class": "title"})[0].text)
                print("Link: " + page_link_songtext)

        except IndexError:
                print("no Songtext found")
                pass
        except requests.exceptions.ReadTimeout:
                print("awkward ReadTimeout error --> Ich muss noch ein bisschen überlegen..")
                print()
                pass


        lines = []
        for line in para:
            if line != "":
                words = line.split(" ")
                lines.append(words)
            else:
                lines.append("ABSATZ")

        return(lines)