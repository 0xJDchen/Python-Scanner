from common import *
THREADNUM = 8

def portTest(ip,port,num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    i  = 0
    while i <num:
        try:
            myport = i + port
            s.connect(( "%s" %ip, myport ))
            s.close()
            print "%s:%d is open" % (ip,myport)
        except BaseException,e:
            pass
        i = i+1
                   
        
def TcpConnect(subnet,port,num=1):
    
    Port = int(port)
    if num > 8:
        for ip in IPNetwork(subnet):
            for i in range(0,THREADNUM):
                t = threading.Thread(target=portTest, args=(ip,Port+i*num/THREADNUM,num/THREADNUM))  
                t.start()              
    else:
        for ip in IPNetwork(subnet):
            portTest(ip,Port,num)
