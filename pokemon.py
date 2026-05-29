
#Hans
#Make pokemon game

#Init
global lv
global x
global day
global win
lv = 1
x=1
import random
#Functions
def Pokemon():
    print((r"                            _\n"))
    print((r"                         .\"' `..._\n"))
    print((r"                        '         `.\n"))
    print((r"                      .'      ___..'\n"))
    print((r"                _   .\"       '   .__,-.,\"\", ,----.\n"))
    print((r"     ,.-\"\"''-..\" :  :        `--'        ' :      :\n"))
    print((r"   .'            :_,'                    `._`\"--. ;\n"))
    print((r"   :              _,.--'\"'\"\"`--._           `.  `\"\n"))
    print((r"  j             ,'               `-.      ,._.'  ,\"\".\n"))
    print((r"  :           ,'                   ,-.   .   __  `..'\n"))
    print((r"  `--.    .'.'                   ,'   `. :_,\"  `.\n"))
    print((r",.   ;   .   \\                 ,'      |         `.\n"))
    print(("' :  :    |    `.             ,'        |\\         `.  _\n"))
    print((r"`.   ._  |      \\         _.'          | .      ___ `\" :\n"))
    print((r"       : '     . \\      ,'  .          ' |     :   `...'\n"))
    print((r"      ,'  \\       `.   .             ,'  |     '  __\n"))
    print((r"     .    `.       |    \\          .'    '    .  (  `.\n"))
    print((r"   .'      \\`.___,'      `-.____.-'     '     :   `-.'\n"))
    print((r"    .   ,\". \\ ..___              _     /      :    .\n"))
    print((r"    :   . :  \\|/\\  `\"'--------+\"|,'  ,'       `-..' :\n"))
    print((r"     `-\" .'   `: `\"-.._______,.\\|  .'               '\n"))
    print((r"         `--. _ `._             _,'        ,\"\"-.__,'\n"))
    print((r"             \" :   `\"--.....--\"'     __   .\n"))
    print((r"             ,-'                 ,.-\"  `-'\n"))
    print((r"            :   ,..             .    ,\"\".\n"))
    print((r"           .'   .  :   __..._   `\"-. :   :\n"))
    print((r"           `.._  : ' ,'      `\"--..' `--\"\n"))
    print((r"               `-' `\" mh\n"))

def Pokemon2():
    print((r"              -._                                   _.\n"))
    print((r"               \\ `-.._                           _,' |\n"))
    print((r"                \\     `-._    _,.--------.._  _.\"    '\n"))
    print((r"                 \\        `--'              ``.     /\n"))
    print((r"                  \\                                j    __\n"))
    print(("__         __       \\                               |.-\"' /\n"))
    print((r"`.`-.`-.__`.`'\"----\"\\                              |    /\n"))
    print((r"   `.       `.       '        ._                       /\n"))
    print((r"   `..        \\               | `.               /|   /\n"))
    print((r"     `.        `.             |   `._          .' |  /\n"))
    print((r"       `.  .-----`            |      `.       /   ' '\"\"''\n"))
    print((r"         `. `.            .    ._      `_    /  ,'    .'\n"))
    print((r"           `. `.           `._   `'\"\"'\"'     \"\"' ,  ,'\n"))
    print((r"             `. `.          `.`.              ,-/ ,'       _..\n"))
    print((r"               `. `.          \\|,---..  ,--\"./ / ,--------\".  \\\n"))
    print((r"                 `._           `.     `/ , .`.',:           \\  \\\n"))
    print((r"                    `._          `..\".,./ ' _.' :            \\  `.\n"))
    print((r"                  ,-'\" `-._              _.\"     .   |.-\"`.   \\  |\n"))
    print((r"                 .         `-..........-'        |   `..   \\   |_'\n"))
    print((r"                 |           `\".                 `.._   .  '  ,'\n"))
    print((r"                 |         |   |                     `\"'    .'\n"))
    print((r"                 |   /\\    |'  '\n"))
    print((r"                 '  /  \\   ||   .\n"))
    print((r"                '   \\  '   |'   ;\n"))
    print((r"                 \\  '  \\   `...'\n"))
    print((r"                  `\"\"   `,' mh\n"))

def Pokemon3():
    print((r"                |`._         |\\\n"))
    print((r"                `   `.  .    | `.    |`.\n"))
    print((r"                 .    `.|`-. |   `-..'  \\           _,.-'\n"))
    print((r"                 '      `-. `.           \\ /|   _,-'   /\n"))
    print((r"             .--..'        `._`           ` |.-'      /\n"))
    print((r"              \\   |                                  /\n"))
    print((r"           ,..'   '                                 /\n"))
    print((r"           `.                                      /\n"))
    print((r"           _`.---                                 /\n"))
    print((r"       _,-'               `.                 ,-  /\"-._\n"))
    print((r"     ,\"                   | `.             ,'|   `    `.\n"))
    print((r"   .'                     |   `.         .'  |    .     `.\n"))
    print((r" ,'                       '   ()`.     ,'()  '    |       `.\n"))
    print(("'-.                    |`.  `.....-'    -----' _   |         .\n"))
    print((r"/ ,   ________..'     '  `-._              _.'/   |         :\n"))
    print((r"` '-\"\" _,.--\"'         \\   | `\"+--......-+' //   j `\"--.. , '\n"))
    print((r"   `.'\"    .'           `. |   |     |   / //    .       ` '\n"))
    print((r"     `.   /               `'   |    j   /,.'     '\n"))
    print((r"       \\ /                  `-.|_   |_.-'       /\\\n"))
    print((r"        /                        `\"\"          .'  \\\n"))
    print((r"       j                                           .\n"))
    print((r"       |                                 _,        |\n"))
    print((r"       |             ,^._            _.-\"          '\n"))
    print((r"       |          _.'    `'\"\"`----`\"'   `._       '\n"))
    print((r"       j__     _,'                         `-.'-.\"`\n"))
    print((r"         ',-.,' mh\n"))

def evolution1():
    print("Your pokemon is evolving!")
    Pokemon2()
    print("Your Gastly has now evolved into a Haunter!")
def evolution2():
    print("Your pokemon is evolving!")
    Pokemon3()
    print("Your Hunater has now evolved into a Haunter!")
    random.randint(.1,1)


def main(lv,x):
    while True:
        print(f"Day {x}!")
        day = input("What would you like to do today? train, rest, battle, or exit: ")
        if day == "train":
            print("Your pokemon has done to do 100 push ups")
            lv = lv + 1
            print(f"Your pokemon is now level {lv}!")
            if lv == 15:
                evolution1()
            if lv == 25:
                evolution2()
            x = x + 1
        if day == "rest":
            print("INFO CARD")
            print(f"level: {lv}")
            print("Gastly")
            Pokemon()
        if day == "rest" and lv >= 15 < 25:
            print("INFO CARD")
            print(f"level: {lv}")
            print("Haunter")
            Pokemon2()
        if day == "rest" and lv >= 25:
            print("INFO CARD")
            print(f"level: {lv}")
            print("Gengar")
            Pokemon3()
        if day == "battle":
            battle = input("Regular battle or Boss fight?: ")
            if battle == "regular battle":
                print("You will now fight a gym member")
            win = random.randint(1,10)
            if win == 1 or 2 or 3 or 4 or 5:
                print("You won")
                lv = lv + 1
                print(f"Your pokemon is now level {lv}!")
            if win == 6 or 7 or 8 or 9 or 10:
                print("You lost")
                lv = lv + 0
                print(f"Your pokemon has stayed at level {lv}!")
            if battle == "boss fight":
                print("You will now fight a boss")
            if win == 1 and lv < 15:
                print("You won!")
                lv = lv + 3
                print(f"Your pokemon is now level{lv}!")
            if lv < 15 and win == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
                print("You lost")
                lv = lv + 0
                print(f"Your pokemon has stayed at level {lv}")
            if lv >= 15 and lv < 25 and win == 1 or 2 or 3 or 4:
                print("You won!")
                lv = lv + 2
                print(f"Your pokemon is now level {lv}")
            if lv >=15 and lv < 25 and win == 5 or 6 or 7 or 8 or 9 or 10:
                print("You lost")
                lv = lv + 0
                print(f"Your level has stayed at level {lv}")
            if lv >= 25 and win == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
                print("You won!")
                lv = lv + 2
                print(f"Your pokemon is now level {lv}")
            if lv >= 25 and win == 9 or 10:
                print("You lost")
                lv = lv + 2
                print(f"You pokemon is now level {lv}")
        if day == "exit":
            print("Thank you for playing")
            break


main(lv,x,)



