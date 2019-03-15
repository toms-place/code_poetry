from bs4 import BeautifulSoup
from src import getWord, getLines
import requests
import random
from random import randint
import json
import time

class newPoet:
    def __init__(self, name):
        self.name = name
        print()
        print(" --------------------------------------------------------------------------------")
        print("|   Hallo, mein Name ist " + name + "!                                          ")
        print("|   Ich bin ein poeti.                                                           |")
        print("|   Ein poeti kann Texte oder Worte zu anderen (besseren?) Texten verarbeiten.   |")
        print(" --------------------------------------------------------------------------------")
        print()



    def saySomething(self):
        print()
        print("Synonym:  " + getWord.Synonym(self.word))
        print()
        print("Reim:     " + getWord.Rhyme(self.word))
        print()



    def collectSomeWords(self):
        flag = True
        self.words = []

        while flag == True:
            elem = input("Gib mir ein Wort! \n")
            if elem == "stop" or elem == "no" or elem == "nein":
                flag = False
            else:
                self.words.append(elem)
                print()
        try:
            self.word = random.choice(self.words)
            print()
            print("---------------------------------------------------")
            print("Unser Wort des Tages: " + self.word)
            print("---------------------------------------------------")
        except IndexError:
                print("no Input")
                pass



    # Gibt das eingegebene Wort, ein dazupassendes Synonym und ein dazupassenden Reim aus.
    def wsr(self, *words):
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
    def file2poetry(self, filepath, option, density):
        lines = getLines.fromFile(filepath)
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
                newLines.append("---------")

        string = "\n"
        for line in newLines:
            for word in line:
                string += word + " "
            string += "\n"
        print(string)


    #
    def wortWechsel(self, amount=10, word="no word"):
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