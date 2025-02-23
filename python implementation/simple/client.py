import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("localhost" , 8000))

client_socket.send("this is the message".encode())

data = client_socket.recv(1024).decode()
print(f"Server says {data}")

client_socket.close()