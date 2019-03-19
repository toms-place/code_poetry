import random

flag = 0
maxWords = 3
words = []

while flag < int(maxWords):
    elem = input("Give me Input number " + str(flag+1) + "!\n")
    words.append(elem)
    flag += 1

print(
    "\n\n\n----------\n\n\n"
    + "Ich treffe "
    + random.choice(words)
    + " "
    + random.choice(words)
    + " "
    + random.choice(words)
    + "\n\n\n----------\n\n\n"
)
