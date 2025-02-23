import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("localhost",9000))
server_data = client_socket.recv(1024).decode()
print(server_data)

while(True):
    data = input()
    client_socket.send(f"{data}".encode())
    server_data = client_socket.recv(1024).decode()
    print(f"Server : {server_data}")
    if(server_data == "closing connection"):
        break

client_socket.close()