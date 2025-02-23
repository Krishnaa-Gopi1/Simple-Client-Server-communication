# Simple-Client-Server-communication

TCP Server-Client using python

**Simple**

**server.py** <br />
1.socket created (server_socket)(socket.SOCK_STREAM->TCP)<br />
2.socket binded to address<br />
3.server_socket listens upto 5 clients<br />
4.server connects to client_socket<br />
5.server recieves data and decodes data<br />
6.close sockets<br />
<br /><br />

**client.py** <br />
1.socket created (client_socket)(socket.SOCK_STREAM->TCP)<br />
2.connect to server_socket<br />
3.send data to server after encoding<br />
4.recieve data from server and decode<br />
5.close socket<br />
<br />

---

<br />

**TCP Server-Client using C**<br />
