import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("localhost" , 8000))

server_socket.listen(5)
print("server listening on port 8000")

client_socket , client_address = server_socket.accept()
print(f"connection established from {client_address}")

data = client_socket.recv(1024).decode()
print(f"data recieved : {data}")

client_socket.send("Message recieved.".encode())

client_socket.close()
server_socket.close()


