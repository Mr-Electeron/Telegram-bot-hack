import requests
import platform
import time
import sys
from colorama import Fore,init
init()

time.sleep(1)
print(Fore.RED+"\nDos Bot Telegram Electron ! ")
time.sleep(1)
print(Fore.GREEN+ "\n L o a d i n g . . . ")
time.sleep(1)
Token = input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Enter your token bot : ")
time.sleep(1)

namber = input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Enter your id telegram : ")
time.sleep(1)

text = input("\n"+Fore.GREEN+"["+Fore.WHITE+"+"+Fore.GREEN+"]"+Fore.WHITE+" Enter your message text : ")
time.sleep(2)

url = ("https://api.telegram.org/bot")+(Token)+("/sendmessage?chat_id=")+(namber)+("&text=")+(text)

dict_info = {"UrlBox":url,
"AgentList":"Mozilla Firefox",
"VersionList":"HTTP/1/1",
"MethodList":"GET"
      }
Dos = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=dict_info)

print(Fore.YELLOW+" \n[ S  T  A  R  T ] \n")

time.sleep(0.5)

print(Dos)

if Dos == "<Response [200]>":
    print(Fore.GREEN+"[+]"+Fore.WHITE+" SENT TEXT MESSAGE :"+ ( text))
if Dos == "<Response [404]>":
    print(Fore.RED+"[-]"+Fore.WHITE+" Eror 404 ")

time.sleep(2)
sys.exit()