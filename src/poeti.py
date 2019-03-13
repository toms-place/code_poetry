from bs4 import BeautifulSoup
from src import getWord, getLines
import requests
import random
from random import randint
import json

class newPoet:
    def saySomething(self, word):
        print(getWord.Synonym(word))

    #Gibt das eingegebene Wort, ein dazupassendes Synonym und ein dazupassenden Reim aus.
    def wsr(self, words):
        for word in words:
            print("Wort: " + word)
            print("Synonym: " + getWord.Synonym(word))
            print("Reim: " + getWord.Rhyme(word))
    
    #Wandelt von einem Text zufällige Wörter in Reimwörter oder Synonyme um und gibt diesen dann aus.
    def text2poetry(self, filepath, option, density):
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