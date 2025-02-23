import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("localhost",9000))

server_socket.listen(5)

client_socket , client_address = server_socket.accept()
client_socket.send("chat started".encode())
while(True):
    data = client_socket.recv(1024).decode()
    print(f"Client : {data}")
    if(data=="stop"):
        client_socket.send("closing connection".encode())
        break
    else:
        send_data = input()
        client_socket.send(data.encode())
        if(send_data == "closing connection"):
            break

client_socket.close()
server_socket.close()

    
