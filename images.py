#Images
#Tutorial on how to open images using python
#2/23

#Initalize
import webbrowser

#Functions


#Main
url = ["https://tinyurl.com/4pwu8dpt", "https://tinyurl.com/bdftjzhp", "https://tinyurl.com/v3wbtyss","https://tinyurl.com/3emy6z2f"]

descriptions = ["This place is perfect to go to if you want to get your summer tan on. In Hawaii you don't gotta worry about the snow sitting on your drive way since its hot all the time.","Japan is the perfect place to go to during the spring time, it's perfect weather makes you feel welcomed and warm and the cherry blossom add to the atmosphere.","Greece is where you wanna go during fall for that nice breezy chill and perfect for nice mornign walks.", "Switzerland is the perfect place to go to during winter because the plenty fun you have with sking and nice welcoming towns."]

def vacation():
    place = input("Do you prefer hotter weather or colder weather?: ")
    if place == "hotter weather":
        country = input("Would you prefer to stay in the United States or travel to a different continent?: ")
        if country == "stay in the United States":
            webbrowser.open(url[0])
            print(descriptions[0])
        if country == "different continent":
            webbrowser.open(url[1])
            print(descriptions[1])
    if place == "colder weather":
        country = input("Do you prefer long walks or skiing?")
        if country == "long walks":
            webbrowser.open(url[2])
            print(descriptions[2])
        if country == "skiing":
            webbrowser.open(url[3])
            print(descriptions[3])


vacation()




#Photo of Hawaii
#Author: Shane Myers
#Article name: Hawaii
#Website name: Matador Network

#Photo of Japan
# Author: United States Department of State
# Date: Febuarary 2026
# Article name: Japan

#Photo of Greece
# Author: Unknown
# Date: March 31, 2021
# Articel name: The most amazing places Autumn in Greece
# Website name: Greece High Definition

#Photo of Switzerland
# Author: Unknown
# Date: Feb 26, 2024
# Website name: Safetravelkit
# Article name: BEST PLACES TO VISIT IN SWITZERLAND IN WINTER
