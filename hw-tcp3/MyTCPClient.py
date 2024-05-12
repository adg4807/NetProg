import socket

# 서버 주소 및 포트 번호 설정
server_address = '127.0.0.1'
port = 80

# 요청할 파일들
files = ['index.html', 'iot.png', 'favicon.ico']

def send_request(filename):
    # 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 서버에 연결
    client_socket.connect((server_address, port))
    
    # HTTP GET 요청 메시지 생성
    request_message = f'GET /{filename} HTTP/1.1\r\nHost: {server_address}\r\n\r\n'
    
    # 요청 보내기
    client_socket.send(request_message.encode())
    
    # 서버로부터 응답 받기
    response = client_socket.recv(4096).decode()
    
    # 응답 출력
    print(f'Requesting {filename}...')
    print(f'Response from server:\n{response}\n')
    
    # 소켓 닫기
    client_socket.close()

for file in files:
    send_request(file)