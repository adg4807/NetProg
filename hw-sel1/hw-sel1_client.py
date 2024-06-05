import socket
import threading

# Constants
PORT = 2500
BUFFER = 1024

# Handler to receive messages from the server
def handler(sock):
    while True:
        try:
            msg = sock.recv(BUFFER)
            if not msg:
                break
            print(msg.decode())
        except:
            break

# Main client function
def main():
    svr_addr = ('localhost', PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(svr_addr)

    my_id = input('ID를 입력하세요: ')
    sock.send(('[' + my_id + ']').encode())

    th = threading.Thread(target=handler, args=(sock,))
    th.daemon = True
    th.start()

    while True:
        msg = '[' + my_id + '] ' + input()
        sock.send(msg.encode())

if __name__ == "__main__":
    main()