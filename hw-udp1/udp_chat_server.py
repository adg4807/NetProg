# server.py
from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

mailboxes = {}

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    message = data.decode()
    print('<- ', message)
    
    if message.startswith('send '):
        parts = message.split(' ', 2)
        if len(parts) < 3:
            response = "Error: Invalid send command"
        else:
            mboxID = parts[1]
            msg = parts[2]
            if mboxID not in mailboxes:
                mailboxes[mboxID] = []
            mailboxes[mboxID].append(msg)
            response = "OK"
    
    elif message.startswith('receive '):
        parts = message.split(' ')
        if len(parts) < 2:
            response = "Error: Invalid receive command"
        else:
            mboxID = parts[1]
            if mboxID in mailboxes and len(mailboxes[mboxID]) > 0:
                response = mailboxes[mboxID].pop(0)
            else:
                response = "No messages"
    
    elif message == 'quit':
        response = "Server shutting down"
        sock.sendto(response.encode(), addr)
        break
    
    else:
        response = "Error: Unknown command"

    sock.sendto(response.encode(), addr)

sock.close()