import socket
import sys
def printMachineInfo():
    host_name=socket.gethostname()
    for i in range(2,10):
        ip_address=socket.gethostbyname(f'Lab7-ST{i:02d}')
        print(host_name)
        print(ip_address)

def find_service_name(ls,protocolName):
    
    for port in ls:
        try:
            gs=socket.getservbyport(port,protocolName)
            print(f"port = {port} service name = {gs}")
        except:
            pass
            
    gs=socket.getservbyport(53,protocolName)
    print(f"port = {53} service name = {gs}")

def connectIP():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as msg:
        print("Failed", msg[1])
        sys.exit()
    print('socket created')
    host='localhost'
    port=80
    try:
        remote_ip=socket.gethostbyname(host)
    except socket.gaierror:
        print('hostname could not be resolved. Exiting')
        sys.exit()
    print(f'IP address {host} is {remote_ip}')
    s.connect((remote_ip,port))
    print(f'Socket connected to {host} on ip {remote_ip}')


def server1():
    sock=socket.socket()
    hostName=socket.gethostname()
    port=21000
    
##    hostName_='Lab7-ST04'
##    hostName=socket.gethostbyname(hostName_)
    print(hostName)
    sock.bind((hostName,port))
    sock.listen(10)
    while True:
        con,address=sock.accept()
        print("I'm now connect to ", address)
        msg="Python Networking"
        con.send(msg.encode("UTF-8"))
    con.close()
def client1():
    sock=socket.socket()
    hostName=socket.gethostname()
    port=21000
    sock.connect((hostName,port))
    r=sock.recv(1024)
    print(r)

def serverChat():
    sock=socket.socket()
##    LOCALHOST='localhost'
    hostName=socket.gethostname()
    port=8080
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((hostName,port))
    server.listen(1)
    print('server started')
    print('waiting for client request..')
    con,address=server.accept()
    print('connected client: ', address)
    msg=''
    while True:
        in_data=con.recv(1024)
        msg=in_data.decode()
        if msg=='bye':
            break
        print("From client ", msg)
        out_data=input("enter msg = ")
        con.send(bytes(out_data,'UTF-8'))
    print('Client disconnected')
    con.close()    
def clientChat():
##    SERVER='localhost'
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    hostName=socket.gethostname()
    port=8080
    client.connect((hostName,port))
    client.sendall(bytes('This is from client','UTF-8'))
    while True:
        in_data=client.recv(1024)
        print("From server:", in_data.decode())
        out_data=input("enter client message: " )
        client.sendall(bytes(out_data,'UTF-8'))
        if out_data=='bye':
            break
    print('Serer disconnected')
    client.close()

if __name__=="__main__":
    serverChat()





##    ls=list(range(0,2**16-1))
##    pn='tcp'
##    find_service_name(ls,pn)
##    pn='UDP'
##    find_service_name(ls,pn)

    
##    printMachineInfo()
##    try:
##        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##    except socket.error as msg:
##        print("Failed", msg[1])
##        sys.exit()
##    print('socket created')
    
