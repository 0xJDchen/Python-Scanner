from common import *
from IPHead import *
from TCPHead import *

def CreateTCPnull(src_ip,dst_ip,dst_port):
    try:
        s = CreateSocket()
        s.settimeout(1)
        ipHead = CreateIpHeader(src_ip,dst_ip)
        flag = createTcpFlag()
        tcpHead = create_tcp_header(src_ip,dst_ip,dst_port,flag)
        buffer = ipHead + tcpHead
        s.sendto(buffer,(dst_ip, dst_port))
    
        data = s.recvfrom(1024) [0][0:]
        tcp = TCP(data[20:40])
        
    except:
	print "%s:%d is open" %(dst_ip,dst_port)

if __name__ == '__main__':
    CreateTCPack(HOST,"10.10.10.143",22)
