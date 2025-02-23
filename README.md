# Simple-Client-Server-communication

TCP Server-Client using python

<u>Simple<u>

server.py
1.socket created (server_socket)(socket.SOCK_STREAM->TCP)
2.socket binded to address
3.server_socket listens upto 5 clients
4.server connects to client_socket
5.server recieves data and decodes data
6.close sockets

client.py
1.socket created (client_socket)(socket.SOCK_STREAM->TCP)
2.connect to server_socket
3.send data to server after encoding
4.recieve data from server and decode
5.close socket

------------------

TCP Server-Client using C