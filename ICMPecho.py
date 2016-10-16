from common import *
from ICMPHead import *
from IPHead import *

magic_message = "JDchen's Scanner!"

def udp_sender(subnet,magic_message):  
    time.sleep(5)   
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    for ip in IPNetwork(subnet):  
        try:  
            sender.sendto(magic_message, ("%s" % ip, 65211))  
        except:  
            pass
  
def ICMPecho(subnet):
    if  os.name == "nt":  
        socket_protocol = socket.IPPROTO_IP  
    else:  
        socket_protocol = socket.IPPROTO_ICMP     
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)       
    sniffer.bind((HOST, 0)) 
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)  
    if os.name == "nt":  
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)      
    t = threading.Thread(target=udp_sender, args=(subnet,magic_message))  
    t.start()      
    try:  
        while True:  
            raw_buffer =  sniffer.recvfrom(65565)[0]  
            ip_header = IP(raw_buffer[0:20])  
            if ip_header.protocol == "ICMP":  
                offset = ip_header.ihl * 4        
                buf = raw_buffer[offset:offset+sizeof(ICMP)]    
                icmp_header = ICMP(buf)  
                if icmp_header.type == 3 and icmp_header.code == 3:  
                    if IPAddress(ip_header.src_address) in IPNetwork(subnet):   
                        if raw_buffer[len(raw_buffer) - len(magic_message):] == magic_message:  
                            print "Host Up: %s" % ip_header.src_address  
    except  KeyboardInterrupt:  
        
        if os.name == "nt":  
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)      
