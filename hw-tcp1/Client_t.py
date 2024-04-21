import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)


name = "Jeong Ah Lee"
sock.send(name.encode())

data = sock.recv(4)  
student_id = int.from_bytes(data, byteorder='big')
print("Received student ID:", student_id)

sock.close()
