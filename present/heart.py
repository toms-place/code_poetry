import time

size = 30

def heart():
    for i in range(size):
        line = ""
        for x in range(size):
            if i == 0:
                if int(size/3) == x or int((size/3 + 1)) == x or int((size/3 - 1)) == x or int(size/3 + size/3) == x or int((size/3 + size/3 + 1)) == x or int((size/3 + size/3 - 1)) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 1:
                if int(size/3 - 2) == x or int((size/3 + 2)) == x or int(size/3 + size/3 - 2) == x or int((size/3 + size/3 + 2)) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 2:
                if int(size/3 - 3) == x or int((size/3 + 3)) == x or int(size/3 + size/3 - 3) == x or int((size/3 + size/3 + 3)) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 3:
                if int(size/3 - 4) == x or int((size/3 + 4)) == x or int(size/3 + size/3 - 4) == x or int((size/3 + size/3 + 4)) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 4:
                if int(size/3 - 5) == x or int((size/3 + 5)) == x or int(size/3 + size/3 - 5) == x or int((size/3 + size/3 + 5)) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 5:
                if int(size/3 - 5) == x or int(size/3 + size/3 + 5) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 6:
                if int(size/3 - 5) == x or int(size/3 + size/3 + 5) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 7:
                if int(size/3 - 5) == x or int(size/3 + size/3 + 5) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 8:
                if int(size/3 - 4) == x or int(size/3 + size/3 + 4) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 9:
                if int(size/3 - 3) == x or int(size/3 + size/3 + 3) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 10:
                if int(size/3 - 2) == x or int(size/3 + size/3 + 2) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 11:
                if int(size/3 - 1) == x or int(size/3 + size/3 + 1) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 12:
                if int(size/3) == x or int(size/3 + size/3) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 13:
                if int(size/3 + 1) == x or int(size/3 + size/3 - 1) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 14:
                if int(size/3 + 2) == x or int(size/3 + size/3 - 2) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 15:
                if int(size/3 + 3) == x or int(size/3 + size/3 - 3) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 16:
                if int(size/3 + 4) == x or int(size/3 + size/3 - 4) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            elif i == 17:
                if int(size/3 + 5) == x or int(size/3 + size/3 - 5) == x:
                    line += ("[•]")
                else:
                    line += ("[ ]")
            else:
                line += ("[ ]")
        print(line)

    

for i in range(1):
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    heart()
    time.sleep(1)