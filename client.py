import socket               # Import socket module

def sendControlMsg(message):
	s = socket.socket()         # Create a socket object
	host = '10.129.23.101' # Get local machine name
	port = 12345                # Reserve a port for your service.

	s.connect((host, port))
	s.send(message)
	#print s.recv(1024)
	s.close()                     # Close the socket when done


sendControlMsg("3")