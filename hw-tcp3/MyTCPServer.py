from socket import *

def handle_client_connection(client_socket):
    # 클라이언트로부터 받은 데이터를 읽어들임
    request = client_socket.recv(1024).decode()

    # HTTP 요청 라인을 파싱하여 요청한 파일 이름 획득
    filename = request.split(' ')[1][1:]

    # 요청한 파일이 존재하는지 확인
    try:
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mime_type = 'text/html'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mime_type = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mime_type = 'image/x-icon'
        else:
            raise FileNotFoundError

        # 요청한 파일이 존재하는 경우 200 OK 응답 반환
        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Type: {}\r\n\r\n'.format(mime_type)
        client_socket.send(response_header.encode())

        # 파일 내용을 클라이언트에게 전송
        if 'text' in mime_type:
            client_socket.send(f.read().encode('utf-8'))
        else:
            client_socket.send(f.read())

        f.close()
    except FileNotFoundError:
        # 요청한 파일이 존재하지 않는 경우 404 Not Found 응답 반환
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        response += '<BODY>Not Found</BODY></HTML>'
        client_socket.send(response.encode())

    # 클라이언트 소켓 닫기
    client_socket.close()

# 웹 서버 소켓 설정
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 80))
server_socket.listen(5)

print('웹 서버가 시작되었습니다.')

while True:
    # 클라이언트의 연결 요청을 수락하고 클라이언트 소켓과 주소를 반환
    client_socket, addr = server_socket.accept()
    print('클라이언트로부터 연결 요청이 들어왔습니다:', addr)

    # 클라이언트 요청을 처리하는 함수 호출
    handle_client_connection(client_socket)