# -*- coding: UTF-8 -*-
import socket
import colorama
from datetime import datetime
from os import system
from colorama import Fore, Back, Style
colorama.init()

system("cls")

msg =       "#######                        ##        ######\n"                                            
msg = msg + "########                       ##       ## ####\n"                                            
msg = msg + "##    #                        ##      ##    ##\n"
msg = msg + "##    #   ######   ### ####  ########  ##     #    #######  ######   ########\n"               
msg = msg + "##   ##  ##   ##     ###  #    ##       ####     ##    ##       ##    ##   #\n"               
msg = msg + "######   #     ##    ##        ##        #####   ##     #    #####    #    #\n"               
msg = msg + "##       #      #    #         ##            ##  #         #######    #    #\n"               
msg = msg + "##       ##    ##    #         ##      #     ##  ##        #    ##    #    #\n"               
msg = msg + "#####     ###  ##   ######      ##  ### ###  ##   ###   ##  ##  ####  ###  ###\n"              
msg = msg + "#####      #####    #######      #####  ######     ######   ######## ####  ###\n"  
msg = msg + "******************************************************************* by S2MMERS\n"

print (msg)

ip = raw_input("Enter IP/Domain: ")
portlist = [20,21,22,23,25,80,443,445,3389]
print ("\nScanning %s \n" %(ip))
t1 = datetime.now()
for port in portlist:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip, port)) == 0:
		print (Fore.GREEN + "\tPort: %s Opened" %(port))
	else:
		print (Fore.RED + "\tPort: %s Closed" %(port))
		
t2 = datetime.now()
total = t2 - t1

print (Fore.WHITE + "\nScan completed in %s" %(total))
	