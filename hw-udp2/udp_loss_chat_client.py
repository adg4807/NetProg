from socket import *
import time

server_addr = ('localhost', 3333)
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    # 클라이언트에서 서버로 보낼 메시지 입력
    msg = input('-> ')
    reTx = 0

    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), server_addr)
        sock.settimeout(2)  # 2초 동안 'ack'을 기다림

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                break
        except timeout:
            reTx += 1
            continue

    if reTx > 5:
        print('Failed to send message.')
        continue
    
    # 서버로부터의 응답 메시지 수신
    sock.settimeout(None)  # 무한정 대기
    response_data, addr = sock.recvfrom(BUFF_SIZE)
    print('<-',  reTx,response_data.decode())