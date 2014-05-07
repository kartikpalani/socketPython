import socket

s= socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(2)

while True:
	conn, addr = s.accept()
	print "got a connection from: ", addr
	print conn.recv(1024)
	conn.send("thanks for connecting")
	conn.close()