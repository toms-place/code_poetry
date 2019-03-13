from src import poeti

def main():
    #Poeti().wsr(["weinen", "fließen", "scheinen", "sprießen"])
    Thomas = poeti.newPoet()
    Thomas.text2poetry("texte/nena.txt", "reim", 3)

main()