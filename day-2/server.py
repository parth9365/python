#import a socket module
import socket

a = raw_input("Enter message to send: ")

#create a socket object
s = socket.socket()

#get local machine name
host = socket.gethostname()

# open a port
port = 12313

#bind a port
s.bind((host, port))

#wait for client to connect
s.listen(5)

#establish connection with client
while True:
	c, addr = s.accept()	#client message
	print 'Got Connection from', addr		#client IP
	c.send(a)
	c.close()
	break