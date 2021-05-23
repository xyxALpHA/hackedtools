# coding=utf-8

import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore, Back, Style

print(Fore.GREEN + "EXAMPLE: domain / ip adresi veya url giriniz")
print("____________________________________________")
domain = input(">>>[+]HEDEF URL/İP/DOMAİN GİRİNİZ:")
print(Fore.BLUE + "lütfen sabırla bekleyiniz,{} hedefi taranıyor...".format(domain))
print("sonuc alamazsanız,tekrar tekrar deneyiniz,sunucuda bazen baglantı kopuklukları oluşmaktadır")

url = "https://who.is/dns/{}".format(domain)

r = requests.get(url)
sleep(15)
soup = BeautifulSoup(r.content,"lxml")
bilgi = soup.find_all("div",attrs={"class":"col-md-12 queryResponseBodyKey"})

for bilgiler in bilgi:

    v = bilgiler.text
    veriler = v
    print(bilgiler.text)
    print(Fore.GREEN + "{} hedefine ait sonuçları görüyorsunuz".format(domain))
    #kaydet
    dosya = open("dns_log.txt","a")
    dosya.write(str(veriler))
    dosya.close
    print("[*] BİLGİLER 'dns_log.txt' DOSYASINA KAYDEDİLDİ / PROGRAM KLASÖRÜ")
  
    
