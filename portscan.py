# -*- coding: UTF-8 -*-
import socket
import colorama
import sys
from datetime import datetime
from os import system
from colorama import Fore
colorama.init()

system('clear')

title = """
##### ##### ##### ##### ##### ##### ###### ###     #    
#   # #   # #   #   #   #     #     #    # # #     # 
#   # #   # #   #   #   #     #     #    # #  #    #
####  #   # ####    #   ####  #     ###### #   #   #
#     #   # #  #    #      #  #     #    # #    #  #
#     #   # #   #   #      #  #     #    # #     # #
#     ##### #   #   #  #####  ##### #    # #     ###
****************************************************
:: Escrito por: S2MMERS
:: Versao: 1.0
:: https://github.com/samirmt
****************************************************
"""

print (title)

ip = raw_input("Enter IP/Domain: ")
portlist = [20,21,22,23,25,80,443,445,3389]
print ("\nScanning %s \n" %(ip))
print(portlist)
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
