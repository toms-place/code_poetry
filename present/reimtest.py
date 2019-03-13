l = ["Schwund", "Kund", "Mund", "nasser Hund", "schund"]

key = "Hund"
key2 = "hund"

for word in l:
    i = len(key)
    if (word[-i:] != key) & (word[-i:] != key2):
        print(word)