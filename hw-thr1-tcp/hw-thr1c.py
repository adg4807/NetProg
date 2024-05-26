import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            break

def main():
    server_address = ('localhost', 2500)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    my_id = input('ID를 입력하세요: ')
    sock.send(f"[{my_id}] has entered the chat.".encode())

    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    try:
        while True:
            message = input()
            if message == 'quit':
                sock.send(f"[{my_id}] has left the chat.".encode())
                break
            sock.send(f"[{my_id}] {message}".encode())
    finally:
        sock.close()

if __name__ == "__main__":
    main()