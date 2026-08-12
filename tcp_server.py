#!/usr/bin/python3 

import socket

TCP_IP = "192.168.1.242" #your ip or localhost to test
TCP_PORT = 6996
BUFFER_SIZE = 100 #Buffer Size of Data listening

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#define socket

s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address: ',addr)

while True:
	
	data = conn.recv(BUFFER_SIZE)
	if not data:
		break
	print("Recieved data: ",data)
	conn.send(data) #echo
	
conn.close()
