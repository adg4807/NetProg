import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    
    student_name = client.recv(1024).decode()
    print("Student name:", student_name)

    student_id = 20221302

    client.send(student_id.to_bytes(4, byteorder='big'))
    
    client.close()
