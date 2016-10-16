from ICMPHead import *
from IPHead import *
from ICMPecho import *
from TCPconnect import *
from TCPSyn import *
from TCPfup import *
from TCPNull import *
from TCPAck import *

def usage():
    print "JDchen's scanner"
    print
    print "python Scan.py -ic target_ip   --Scan by ICMP"
    print "python Scan.py -tc target_ip port   --Scan by TCP Socket connect"
    print "python Scan.py -tn target_ip port1 port2 --Scan by TCP Socket connect "
    print "python Scan.py -ts target_ip port  --Scan by TCP Socket SYN"
    print "python Scan.py -tnu target_ip port  --Scan by TCP Socket NULL"
    print "python Scan.py -tfu target_ip port  --Scan by TCP Socket FIN+URG+PSH"
    print "python Scan.py -tac target_ip port  --Scan by TCP Socket ACK"
    
if len(sys.argv) ==1:
    usage()
    exit()
if sys.argv[1] == '-ic':
    ICMPecho(sys.argv[2])
elif sys.argv[1] == '-tc':
    TcpConnect(sys.argv[2],sys.argv[3])
elif sys.argv[1] == '-tn':
    TcpConnect(sys.argv[2],sys.argv[3],int(sys.argv[4]) - int(sys.argv[3]))
elif sys.argv[1] == '-ts':    
    CreateTCPsyn(HOST,sys.argv[2],int(sys.argv[3]))
elif sys.argv[1] == '-tnu':    
    CreateTCPnull(HOST,sys.argv[2],int(sys.argv[3]))
elif sys.argv[1] == '-tfu':    
    CreateTCPfup(HOST,sys.argv[2],int(sys.argv[3]))
elif sys.argv[1] == '-tac':    
    CreateTCPfup(HOST,sys.argv[2],int(sys.argv[3]))
else:
    usage()
    

    
    




