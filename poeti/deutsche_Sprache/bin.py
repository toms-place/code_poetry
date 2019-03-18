from bs4 import BeautifulSoup
from src import getWord, getLines
from random import randint
import random
import time
import os

class ein_Poeti_und_heiße:
    def __init__(self, name):
        self.name = name

        fill = (" "*(55-len(name)) + "|")
        print()
        print(" --------------------------------------------------------------------------------")
        print("|   Hallo, mein Name ist " + name + "!" + fill)
        print("|   Ich bin ein poeti.                                                           |")
        print("|   Ein poeti kann Texte oder Worte zu anderen (besseren?) Texten verarbeiten.   |")
        print(" --------------------------------------------------------------------------------")
        print()



    def kann_etwas_sagen(self):
        print()
        print("Synonym:  " + getWord.Synonym(self.word))
        print()
        print("Reim:     " + getWord.Rhyme(self.word))
        print()



    def brauche_Worte(self):
        flag = True
        self.words = []

        while flag == True:
            elem = input("Gib mir ein Wort!\n")
            if elem == "stop" or elem == "no" or elem == "nein":
                flag = False
            else:
                self.words.append(elem)
                print()
        try:
            self.word = random.choice(self.words)
            print()
            print("---------------------------------------------------")
            print("Mein Wort des Tages: " + self.word)
            print("---------------------------------------------------")
            print()
        except IndexError:
                print("no Input")
                pass



    # Gibt das eingegebene Wort, ein dazupassendes Synonym und ein dazupassenden Reim aus.
    def wandle_das_Wort_zu_Synonym_und_Reim(self, *words):
        print()
        print("------------------")
        print("Wort|Synonym|Reim:")
        print("------------------")
        print()
        wordList = []
        if isinstance(words, list):
            wordList = words
        else:
            if len(words) > 0:
                wordList.append(words)
            else:
                wordList.append(self.word)
        for word in wordList:
            print("Wort:     " + word)
            time.sleep(2)
            print("Synonym:  " + getWord.Synonym(word))
            time.sleep(0.7)
            print("Reim:     " + getWord.Rhyme(word))
            time.sleep(0.7)
            print("Synonym:  " + getWord.Synonym(word))
            time.sleep(0.7)
            print("Reim:     " + getWord.Rhyme(word))
            time.sleep(0.7)
            print("Synonym:  " + getWord.Synonym(word))
            time.sleep(0.7)
            print("Reim:     " + getWord.Rhyme(word))
            time.sleep(0.7)
            print()
            time.sleep(3)



    # Wandelt von einem Text zufällige Wörter in Reimwörter oder Synonyme um und gibt diesen dann aus.
    # Es kann eine der Optionen ["mix", "reim", "synonym"] gewählt werden und die Dichte der zu verändernden Worte gewählt werden.
    def ändere_Text(self, filepath, option, density):
        print()
        print("------------------")
        print("Song: " + filepath.split("/")[1].split(".")[0])
        print("------------------")
        print()
        lines = getLines.fromTXT(filepath)
        newLines = []
        for line in lines:
            if line != "ABSATZ":
                newLine = []
                for word in line:
                    if 1 == randint(1, density):
                        cleanedWord = word.replace("!","").replace(",","").replace(".","").replace("?","").replace(":","").replace(";","").replace("--","")
                        if option == "mix":
                            if 1 == randint(1, 2):
                                newLine.append(getWord.Rhyme(cleanedWord))
                            else:
                                newLine.append(getWord.Synonym(cleanedWord))
                        elif option == "reim":
                                newLine.append(getWord.Rhyme(cleanedWord))
                        elif option == "synonym":
                                newLine.append(getWord.Synonym(cleanedWord))
                        else:
                                newLine.append(getWord.Rhyme(cleanedWord))
                    else:
                        newLine.append(word)
                newLines.append(newLine)
                
            else:
                newLines.append("")

        string = "\n"
        for line in newLines:
            for word in line:
                string += word + " "
            string += "\n"
        print(string)


    # Wandelt ein Wort in ein Synonym und weiter in einen Reim und diesen Reim weiter in ein Synonym und so weiter.
    # Nimmt die Anzahl an Iterationen (Standard ist 10) und ein Wort entgegen.
    def wechsle_das_Wort(self, amount=10, word="no word"):
        print()
        print("-------------")
        print("Wortwechsel:")
        print("-------------")
        print()
        if word == "no word":
            word = self.word
        for i in range(amount):
            if i%2 == 0:
                word = getWord.Synonym(word)
                print("Synonym:    " + word)
            else:
                word = getWord.Rhyme(word)
                print("Reim:       " + word)
            time.sleep(1)
            if i != (amount) - 1:
                print("∫")

    def schreibe_wenn_dann_Sätze(self, amount=5):
        print()
        print("----------------")
        print("Wenn-Dann Sätze:")
        print("----------------")
        print()
        
        nameLines = getLines.fromTXT("./textstelle/de/Vornamen/vornamen.txt")
        verbenLines = getLines.fromTXT(os.path.normpath("./textstelle/de/Verben (untrennbare)/verben.txt"))
        for i in range(amount):
            verb = random.choice(verbenLines)[0]
            print("Wenn " + random.choice(nameLines)[0] + " und " + random.choice(nameLines)[0] + " " + verb + ",")
            print("Dann " + random.choice(verbenLines)[0] + " " + random.choice(nameLines)[0] + " und " + random.choice(nameLines)[0] + " beim " + getWord.Rhyme(verb) + ".")
            print()
            time.sleep(2)


    def schreibe_sei_wie_du_bist_Sätze(self, amount=5):
        print()
        print("----------------")
        print("Sei Sätze:")
        print("----------------")
        print()
        
        personenadjektive = getLines.fromTXT(os.path.normpath("./textstelle/de/Adjektive (die zu Personen passen)/personenadjektive.txt"))
        for i in range(amount):
            adj = random.choice(personenadjektive)[0]
            rhyme = getWord.Rhyme(adj)
            print("+ Sei " + random.choice(personenadjektive)[0] + " und " + adj + ",")
            print("- jedoch nicht " + rhyme + ".")
            time.sleep(2)

    def schreibe_mit_Gefühl(self, amount=5):
        print()
        print("----------------")
        print("Gefühle:")
        print("----------------")
        print()
        
        feelings = getLines.fromYAML(os.path.normpath("./textstelle/de/Gefühle/gefuehle.yaml"))
        for i in range(amount):
            feeling = random.choice(feelings)
            rhyme = getWord.Rhyme(feeling)
            print("Ich empfinde " + random.choice(feelings) + " und " + feeling + ",")
            print("und noch dazu stört mich " + rhyme + ".")
            time.sleep(2)


    def erfinde_Worte(self, amount=10):
        print()
        print("-------------------")
        print("Ikea + Komposition:")
        print("-------------------")
        print()
        
        ikeas = getLines.fromTXT(os.path.normpath("./textstelle/de/IKEA Kategorien/ikea_kategorien.txt"))
        komposits = getLines.fromTXT(os.path.normpath("./textstelle/de/Komposita hinten (Personen)/komposita_hinten_person.txt"))

        for i in range(amount):
            ikea = random.choice(ikeas)[0]
            komposit = random.choice(komposits)[0]
            neuesWort = ikea + komposit
            print(neuesWort)
            print()
            time.sleep(2)

    def konjuguere(self, amount=10):
        print()
        print("-------------------")
        print("Konjugation:")
        print("-------------------")
        print()
        
        print(getWord.Konjugation("spazieren", "ich", "Futur I Konjunktiv II"))