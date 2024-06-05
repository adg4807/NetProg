import socket
import select
import time

# Constants
BUFFER = 1024
PORT = 2500

# Create TCP socket
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)
socks = [s_sock]  # List to keep track of all sockets
print('Server Started')

while True:
    # Wait for any socket to be ready for processing
    r_sock, _, _ = select.select(socks, [], [])
    for s in r_sock:
        if s == s_sock:  # New client connection
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('New client ({}) connected'.format(addr))
        else:  # Data from existing client
            data = s.recv(BUFFER)
            if not data:  # Client disconnected
                print('Client ({}) disconnected'.format(s.getpeername()))
                socks.remove(s)
                s.close()
            else:  # Received data from client
                print(time.asctime() + ' ' + str(s.getpeername()) + ': ' + data.decode())
                for client in socks:
                    if client != s_sock and client != s:
                        try:
                            client.send(data)
                        except:
                            client.close()
                            socks.remove(client)