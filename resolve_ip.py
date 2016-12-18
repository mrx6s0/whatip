#! /usr/bin/env python
# -*- coding: utf-8 -*

import os, time, socket, sys, string

print ("#############################################################")
print ("#     SCRIPT : resolve_ip.py                                #")
print ("#     AUTHOR : MRX                                          #")
print ("#     VERSION: BETA                                         #")
print ("#   DISCOVER THE INTERNAL IP OF ANY HOST, URL, DOMAIN, ETC  #")
print ("#                                                           #")
print ("#             [*] PRE IP SPOOFING [*]                       #")
print ("#############################################################")
print ("")

host = raw_input('WEBSITE LINK TO SNIFF: ')
ip = socket.gethostbyname(host)
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80



def getip():
    try:
        conn.connect((ip, port))
        conn.send("Sending packet confirmation")
    except:   
        print ("")
        print ("############################################################")
        print ("#     STATUS : DOWN                                        #")
        print ("#     IP: " + ip + "                                       #")
        print ("############################################################")
        print ("")
    print ("")
    print ("##############################################################################################")
    print ("#     STATUS : UP!                                                                          ##")
    print ("#     IP: " + ip + "                                                                      ##")
    print ("##############################################################################################")
    print ("")    
    return

getip()
