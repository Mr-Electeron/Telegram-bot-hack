import requests
import platform
import time
import sys
import os
from colorama import Fore,init
os.system("cls")
init()

time.sleep(1)
print(Fore.RED+"\nDos Bot Telegram Electron ! ")
time.sleep(1)
print(Fore.GREEN+ "\n L o a d i n g . . . ")
time.sleep(1)
BOT_NAME= input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Enter your bot name bot : ")
time.sleep(1)

namber = input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Enter your id telegram : ")
time.sleep(1)


url = ("https://t.me/Botfather")+(BOT_NAME)+("/sendtoken?chat_id=")+(namber)

time.sleep(1)
dict_info = {"UrlBox":url,
"AgentList":"Mozilla Firefox",
"VersionList":"HTTP/1/1",
"MethodList":"GET"
      }
Dos = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=dict_info)

print(Fore.YELLOW+" \n[ S  T  A  R  T ] \n")

time.sleep(0.5)

print(Dos)

if Dos.status_code == 200:
    print("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" SENT TEXT MESSAGE : "+ ( text))
else:
    print("\n"+Fore.RED+"["+Fore.WHITE+"+"+Fore.RED+"]"+Fore.WHITE+" Eror 404 ")

time.sleep(2)
sys.exit()
