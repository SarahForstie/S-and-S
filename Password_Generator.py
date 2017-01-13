import json
import time
import random

def main():
    day = time.strftime("%A")
    login = loginGen(day)
    print("login:",login)
    password = getPassword(day)
    print(password)

def loginGen(dayname):
    login_list = []
    login_list.append(dayname)
    login_list.append(time.strftime("%#m"))
    login_list.append(time.strftime("%Y"))
    login = "".join(login_list)
    return login

def getPassword(day):
    word = getWord(day)
    character = genChar()
    number = genNum()
    password = makePassword(word, character, number)
    return password
    
def getWord(dayname):
    RequestURL = "http://www.setgetgo.com/randomword/get.php?len="
    
    if dayname in ("Monday","Tuesday","Wednesday"):
        RequestURL = RequestURL + "8"

    elif dayname in ("Thursday","Friday"):
        RequestURL = RequestURL + "9"

    elif dayname in ("Saturday","Sunday"):
        RequestURL = RequestURL + "10"
        
    return RequestURL

def genChar():
    charlist = ["!","@","£","$","%","&","*","#"]
    character = random.choice(charlist)
    return character

def genNum():
    num = random.randint(1,9)
    num = str(num)
    return num

def makePassword(word, char, num):
    pass_list = []
    pass_list.append(word)
    pass_list.append(char)
    pass_list.append(num)
    print(pass_list)
    password = "".join(pass_list)
    return password

main()
