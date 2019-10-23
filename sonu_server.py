#import socket module

# http://128.238.251.26:6789/HelloWorld.html

from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
HOST = '127.0.0.1'
PORT = 6789

serverSocket.bind((HOST,PORT))
serverSocket.listen(1)
while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		
		filename = message.split()[1]

		f = open(filename[1:])

		outputdata = f.read()

		#Send one HTTP header line into socket
		connectionSocket.send(b'\nHTTP 200 OK\n')

		#Send the content of the requested file to the client

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
			
		connectionSocket.close()
	except IOError:
		print("HelloWorld")
		#Send response message for file not found
		
		connectionSocket.send(b'\n404 File Not Found\n')

		#Close client socket
		serverSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
