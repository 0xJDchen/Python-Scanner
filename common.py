import os  
import struct  
import threading  
import time  
import sys
import socket
import random
from netaddr import IPNetwork,IPAddress  
from ctypes import * 

HOST = "10.10.10.128"

def checksum(msg):  
    s = 0 
 
    for i in range(0,len(msg),2):  
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]))  
        s = s+w  
     
    s = (s>>16) + (s & 0xffff)  
    s = ~s & 0xffff 
     
    return s  


def CreateSocket(source_ip,dest_ip):  
        try:  
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)  
        except socket.error, msg:  
            print 'Socket create error: ',str(msg[0]),'message: ',msg[1]  
            sys.exit()  
         
        s.setsockopt(socket.IPPROTO_TCP, socket.IP_HDRINCL, 1)  
        return s  

