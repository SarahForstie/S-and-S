import json
import requests
import time

def main():
    day = time.strftime("%A")
    login = loginGen(day)
    print(login)
    APIget(day)

def loginGen(dayname):
    login_list = []
    login_list.append(dayname)
    login_list.append(time.strftime("%#m"))
    login_list.append(time.strftime("%Y"))
    login = "".join(login_list)
    return login

def APIget(dayname):
    RequestURL = "http://www.setgetgo.com/randomword/get.php?len="
    
    if dayname in ("Monday","Tuesday","Wednesday"):
        RequestURL = RequestURL + "8"

    elif dayname in ("Thursday","Friday"):
        RequestURL = RequestURL + "9"

    elif dayname in ("Saturday","Sunday"):
        RequestURL = RequestURL + "10"

    response = requests.get(RequestURL)
    print(response)



main()
