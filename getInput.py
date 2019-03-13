import random

flag = True
words = []

while flag == True:
    elem = input("Give me Input! \n")
    if elem != "stop":
        words.append(elem)
    else:
        flag = False

print(random.choice(words))
