import socket

def calculate_expression(expression):
    try:
        result = eval(expression)
        return round(result, 1) if isinstance(result, float) else result
    except Exception as e:
        return str(e)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 3333))
    server_socket.listen(5)

    print("서버가 실행 중입니다.")

    
    client_socket, _ = server_socket.accept()
    print("클라이언트가 연결되었습니다.")

    while True:
        try:
            expression = client_socket.recv(1024).decode()
            print("수신된 계산식:", expression)

            if not expression:
                break

            result = calculate_expression(expression)
            client_socket.send(str(result).encode())
        except ConnectionError as e:
            print("클라이언트와의 연결이 끊어졌습니다.")
            break
        
        except Exception as e:
            print("오류 발생:", e)
            break

    client_socket.close()

if __name__ == "__main__":
    main()