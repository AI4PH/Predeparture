import numpy as np

friendlist = []
namelength = {}
sumlength = 0

def printfriends(friends):
    print("Here are your friends: ")
    for name in friends:
        print(' ', name)

print("*** Warning: this is a shy little whatever that does not offer error checking. Please be nice and kind.")
while True:
    inp = input("Type  quit  to exit, or input name of a friend that you have not inputted before: ")
    if inp == 'quit':
        break
    friendlist.append(inp)
    namelength[inp] = len(inp)
    printfriends(friendlist)

for name in namelength:
    sumlength = sumlength + int(namelength[name])
avelength = sumlength / len(namelength)

if avelength > 6:
    print("*** Wow! Your friends have long names. How unique.")
else:
    print("*** Short names? Well I'm sure your friends have unique personalities but long names are kinda cool too.")


def checkloneliness():
    lonely = np.less(len(friendlist),4)
    if lonely == True:
        print("*** You deserve more love! Go hug some kittens or kiss a dog or maybe find yourself a friend.")
    else:
        print("*** Have you checked on your friends today? Give them a call to see if they are still alive.")
checkloneliness()
