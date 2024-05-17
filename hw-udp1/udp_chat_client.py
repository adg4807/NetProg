# client.py
from socket import *

server_address = ('localhost', 3333)
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('-> ')
    sock.sendto(message.encode(), server_address)
    
    if message == 'quit':
        break
    
    data, _ = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())

sock.close()