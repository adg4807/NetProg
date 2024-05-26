import socket
import threading

clients = []  # 클라이언트 소켓 목록
lock = threading.Lock()  # 클라이언트 목록 보호를 위한 락

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    with lock:
        clients.append(client_socket)
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            message_str = message.decode()
            print(f"Received message from {client_address}: {message_str}")
            if 'quit' in message_str:
                print(f"Client {client_address} disconnected")
                break
            broadcast(message, client_socket)
    finally:
        with lock:
            clients.remove(client_socket)
        client_socket.close()

def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    pass

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 2500))
    server_socket.listen(5)
    print("Server started on port 2500")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()