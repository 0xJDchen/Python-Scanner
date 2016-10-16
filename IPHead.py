from common import *

class IP(Structure):
    
    _fields_ = [
        ("ihl",           c_ubyte, 4),
        ("version",       c_ubyte, 4),
        ("tos",           c_ubyte),
        ("len",           c_ushort),
        ("id",            c_ushort),
        ("offset",        c_ushort),
        ("ttl",           c_ubyte),
        ("protocol_num",  c_ubyte),
        ("sum",           c_ushort),
        ("src",           c_ulong),
        ("dst",           c_ulong)
    ]
    
    def __new__(self, socket_buffer=None):
            return self.from_buffer_copy(socket_buffer)    
        
    def __init__(self, socket_buffer=None):

        # map protocol constants to their names
        self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}
        
        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))
    
        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)
            


        try:  
            self.protocol = self.protocol_map[self.protocol_num]  
        except:  
            self.protocol = str(self.protocol_num)
            
    
def CreateIpHeader(source_ip, dest_ip):  
    packet = '' 
       
    headerlen = 5 
    version = 4 
    tos = 0 
    tot_len = 20 + 20 
    id = random.randrange(18000,65535,1)  
    frag_off = 0 
    ttl = 255 
    protocol = socket.IPPROTO_TCP  
    check = 10 
    saddr = socket.inet_aton ( source_ip )  
    daddr = socket.inet_aton ( dest_ip )  
    hl_version = (version << 4) + headerlen  
    ip_header = struct.pack('!BBHHHBBH4s4s', hl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)  
     
    return ip_header 

if __name__ == '__main__':
    buffer = CreateIpHeader("10.10.10.1","10.10.10.128")
    for i in range(0,20,4):
        print "%2x %2x %2x %2x" % (ord(buffer[i]),ord(buffer[i+1]),ord(buffer[i+2]),ord(buffer[i+3]) ) 

