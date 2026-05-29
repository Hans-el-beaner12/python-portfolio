#Hans
#Hogwarts
#Create a program that prompts the user for their name and simulates being assigned one of the 4 hogwarts houses

#Init
import time
import random
#Functions
def main():
    print("Welcome to Hogwarts")
    name = input("What is your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    print( house(name))
def house(name):
    if name == "Harry" or name == "Hermione" or name == "Ron":
        return "Gryffindor!"
    if name == "Newt" or name == "Nymphadora" or name == "Pomona":
        return "Hufflepuff!"
    if name == "Luna" or name == "Cho" or name == "Fillus":
        return "Ravenclaw!"
    if name == "Voldemort" or name == "Draco" or name == "Severus":
        return "Slytherin!"
    else:
        roll = random.randint(1,4)
        if roll == 1:
            return "Gryffindor!"
        if roll == 2:
            return "Hufflepuff!"
        if roll == 3:
            return "RavenClaw!"
        if roll == 4:
            return "Slytherin!"


main()
