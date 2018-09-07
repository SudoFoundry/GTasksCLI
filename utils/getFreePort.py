# getFreePort.py - Does exactly what the name suggests.
# Not intended for human usage, but you can use it if you want

import socket

def getEmptyPort():
	s = socket.socket() # create new socket
	s.bind(('', 0)) # bind to a port assigned by OS
	port = s.getsockname()[1] # obtains the port assigned by os
	s.close() # closes the socket like a good citizen
	return port

if __name__ == "__main__":
	print(getEmptyPort()) # because the intended use is by a script, I'll print it to the console output
