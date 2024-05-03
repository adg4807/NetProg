import socket

def calculate_expression(expression):
    try:
        result = eval(expression)
        return round(result, 1) if isinstance(result, float) else result
    except Exception as e:
        return str(e)

def main():
        try:
            # 서버에 연결
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 3333))

            while True:
                expression = input("계산식을 입력하세요 (또는 'q'를 입력하여 종료): ")
                if expression.lower() == 'q':
                    break

                # 서버로 계산식 전송
                client_socket.send(expression.encode())

                # 서버에서 결과 수신
                result = client_socket.recv(1024).decode()
                print("결과:", result)

            # 연결 종료
            client_socket.close()
        except ConnectionError as e:
            print("서버와의 연결이 끊어졌습니다. 다시 연결을 시도합니다.")
        except Exception as e:
            print("오류 발생:", e)

if __name__ == "__main__":
    main()