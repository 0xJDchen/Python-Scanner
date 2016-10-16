from common import *

class TCP(Structure):
    _fields_ = [
        ("src_port",         c_ushort),
        ("dst_port",         c_ushort),
        ("seq",     c_ulong),
        ("ack_seq",       c_ulong),
        ("offset",  c_ubyte),
        ("flag", c_ubyte),
        ("windows", c_ushort),
        ("checksum", c_ushort),
        ("point", c_ushort),
    ]
    
    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)    
    
    def __init__(self, socket_buffer):
        pass
    
    def CreateSocket(source_ip,dest_ip):  
        try:  
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)  
        except socket.error, msg:  
            print 'Socket create error: ',str(msg[0]),'message: ',msg[1]  
            sys.exit()  
         
        s.setsockopt(socket.IPPROTO_TCP, socket.IP_HDRINCL, 1)  
        return s  


def checksum(msg):  
    s = 0 
 
    for i in range(0,len(msg),2):  
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]))  
        s = s+w  
     
    s = (s>>16) + (s & 0xffff)  
    s = ~s & 0xffff 
     
    return s  

def createTcpFlag(fin=0,syn=0,rst=0,psh=0,ack=0,urg=0):
    tcp_flags = fin + (syn<<1) + (rst<<2) + (psh<<3) + (ack<<4) + (urg<<5)
    return tcp_flags
    
def create_tcp_header(source_ip, dest_ip, dest_port,tcp_flag):  
 
    source = random.randrange(32000,62000,1)     
    seq = 0 
    ack_seq = 0 
    doff = 5 
 
    window = socket.htons (8192)    
    check = 0 
    urg_ptr = 0 
    offset_res = (doff << 4) + 0 
    tcp_flags = tcp_flag
    tcp_header = struct.pack('!HHLLBBHHH', source, dest_port, seq, ack_seq, offset_res, tcp_flags, window, check, urg_ptr)  
 
    source_address = socket.inet_aton( source_ip )  
    dest_address = socket.inet_aton( dest_ip )  
    placeholder = 0 
    protocol = socket.IPPROTO_TCP  
    tcp_length = len(tcp_header)  
    psh = struct.pack('!4s4sBBH', source_address, dest_address, placeholder, protocol, tcp_length);  
    psh = psh + tcp_header;  
    tcp_checksum = checksum(psh)  
 
  
    tcp_header = struct.pack('!HHLLBBHHH', source, dest_port, seq, ack_seq, offset_res, tcp_flags, window, tcp_checksum, urg_ptr)  
    return tcp_header     

def CreateSocket():  
    try:  
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)  
    except socket.error, msg:  
        print 'Socket create error: ',str(msg[0]),'message: ',msg[1]  
        sys.exit()  
 
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)  
    return s 
    
if __name__ == '__main__':
    buffer = create_tcp_syn_header("10.10.10.1","10.10.10.143",0x80)
    for i in range(0,20,4):
        print "%2x %2x %2x %2x" % (ord(buffer[i]),ord(buffer[i+1]),ord(buffer[i+2]),ord(buffer[i+3]) ) 
        
