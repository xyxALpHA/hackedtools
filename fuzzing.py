# coding=utf-8

import requests
from colorama import Fore, Back, Style

dosya = open("fuzzing.txt","r")
icerik = dosya.read()
dosya.close()
print(Fore.GREEN + "EXAMPLE: http://www.orneksite.com")
print("__________________________________")
hedef = input("[+]>>>URL GİRİNİZ:")
for i in icerik.splitlines():

    print(i,"\n")
    url = hedef+str(i)

    sonuc = requests.get(url=url)
    if "200" in str(sonuc.status_code):
        print(Fore.BLUE + "[*] DOSYA VEYA KLASÖR MEVCUT OLABİLİR:",i,"\n")

    else:
        print(Fore.RED + "[!] DOSYA VEYA KLASÖR MUHTEMELEN YOK:",i,"\n")
