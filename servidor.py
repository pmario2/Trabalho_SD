import socket
HOST = '127.0.01'
PORT = 8001
nlisten = 1
tcp =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST,PORT)
tcp.bind(orig)
while True:
	tcp.listen(nlisten)
	con,cliente = tcp.accept()

	print 'conectou',cliente
	msg = con.recv(192)
	print msg
tcp.close()
