#Ben and Hans code
#Goal: Make a slot machine that randomizes the numbers
#Init
import random

symbols = ["7", "💝", "💝", "💝", "🌟", "🌟", "🌟", "🂡", "🂡", "🂡"]
weights = [90, 10, 10, 10]
slots = []

#Functions
credits = int(input("How many credits would you like to put in the machine?: "))

def slot():
    print("welcome to the 3 slot machine!!")
    global credits
    while True:
        spin = input("yes to spin, quit to quit, each spin is 1 credit: ")
        if spin == "yes":
            credits = credits - 1
            for i in range(3):
                    slots.append(random.choice(symbols))
            print(slots)
            if slots[0] == "7" and slots[1] == "7" and slots[2] == "7":
                 print("You won da big kahuna!!")
                 credits = credits + 1000
                 print(f"You now have {credits} credits. don't stop now, you're five big kahuna's away from youre wife maybe not leaving you! ")
            elif slots[0] == slots[1] and slots[0] == slots[2]:
                 credits = credits + 10
                 print("You won!")
                 print(f"You now have {credits} credits. Youre headed in the right direction.")
            else:
                 print("you lost")
                 print(f"You now have {credits} credits.")
            slots.clear()
        if spin == "quit":
             break
slot()
