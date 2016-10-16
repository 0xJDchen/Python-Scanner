from common import *
from IPHead import *
from TCPHead import *

def CreateTCPsyn(src_ip,dst_ip,dst_port):
    s = CreateSocket()
    ipHead = CreateIpHeader(src_ip,dst_ip)
    flag = createTcpFlag(syn=1)
    tcpHead = create_tcp_header(src_ip,dst_ip,dst_port,flag)
    buffer = ipHead + tcpHead
    s.sendto(buffer,(dst_ip, dst_port))
    data = s.recvfrom(1024) [0][0:]
    tcp = TCP(data[20:40])
    if tcp.flag == 0x12:
        print "%s:%d is open" %(dst_ip,dst_port)
        

