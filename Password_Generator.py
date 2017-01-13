import json
import time
import random
import urllib.request

def main():
    #runs the program.
    day = time.strftime("%A") #called for day in main as multiple functions need it.
    login = loginGen(day) #Creates the login.
    print("login:",login) # To test.
    password = getPassword(day) # Calls a function which calls other functions to put together the password.
    print(password) # To test.

def loginGen(dayname):
    #Generates login as a list then joins the list and returns to main.
    login_list = []
    login_list.append(dayname)
    login_list.append(time.strftime("%#m"))
    login_list.append(time.strftime("%Y"))
    login = "".join(login_list)
    return login

def getPassword(day):
    # Acts as a hub for 4 functions to put together the password.
    word = getWord(day)
    character = genChar()
    number = genNum()
    password = makePassword(word, character, number)
    return password
    
def getWord(dayname):
    #Calls out to external API to get a word. The day name is used to slightly change the URL.
    RequestURL = "http://www.setgetgo.com/randomword/get.php?len="
    
    if dayname in ("Monday","Tuesday","Wednesday"):
        RequestURL = RequestURL + "8"

    elif dayname in ("Thursday","Friday"):
        RequestURL = RequestURL + "9"

    elif dayname in ("Saturday","Sunday"):
        RequestURL = RequestURL + "10"

    response = urllib.request.urlopen(RequestURL)
    myword = response.read().decode("utf-8")
        
    return myword.capitalize()

def genChar():
    #Randomly chooses from a set of characters then returns it.
    charlist = ["!","@","£","$","%","&","*","#"]
    character = random.choice(charlist)
    return character

def genNum():
    #Randomly generates a number and returns it.
    num = random.randint(0,9)
    num = str(num)
    return num

def makePassword(word, char, num):
    #Puts together the password as a list then joins it and returns it.
    pass_list = []
    pass_list.append(word)
    pass_list.append(char)
    pass_list.append(num)
    password = "".join(pass_list)
    return password

main() # Runs program
