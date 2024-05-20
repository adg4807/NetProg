import random
from socket import *

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    if random.random() > 0.5:
        sock.sendto(b'ack', addr)
        print('<-', data.decode())
        
        # 서버에서 클라이언트로 보낼 메시지 입력
        response_msg = input('->')
        sock.sendto(response_msg.encode(), addr)
    else:
        print('Packet loss simulated, no ack sent')