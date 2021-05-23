# coding=utf-8

import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore, Back, Style

print(Fore.GREEN + "EXAMPLE: domain / ip adresi veya url giriniz")
print("____________________________________________")
domain = input(">>>[+]HEDEF URL/İP/DOMAİN GİRİNİZ:")

print(Fore.BLUE + "Lütfen sabırla bekleyiniz,{} hedefi taranıyor...".format(domain))
url = "https://check-host.net/ip-info?host={}".format(domain)

r = requests.get(url)
sleep(15)
soup = BeautifulSoup(r.content,"lxml")
bilgi = soup.find_all("div",attrs={"class":"ipinfo-item"})

for bilgiler in bilgi:

    v = bilgiler.text
    veriler = v
    print(bilgiler.text)
    #kaydet
    dosya = open("ip_log.txt","a")
    dosya.write(str(veriler))
    dosya.close
    print(Fore.GREEN + "[*] BİLGİLER 'ip_log.txt' DOSYASINA KAYDEDİLDİ / PROGRAM KLASÖRÜ")
    

   

   
