import socket
import os
import shutil
HOST = ''
PORT = 8002
nlisten = 100
home_path = '/home/pmario/SD/'
tcp =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST,PORT)
tcp.bind(orig)
tcp.listen(100)
con,cliente = tcp.accept()
		
while True:
	
	msg = con.recv(100)
	msg2 = msg.split('.')
	x = msg2[0]
	path = msg2[1]
	
	if x == '1':
		print 'comando '+ x
	#comando 1: digite pasta + nome 
		dst_dir =home_path + path
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)
	if x == '3':
		print 'comando '+ x
	#comando 3: digite nome do arquivo
		if os.path.isfile(home_path+path):
			os.remove(home_path+path)  # remove the file
	if x == '4':
		print 'comando '+ x
	#comando 4: digite o nome da pasta
		if os.path.isdir(home_path+path):
			shutil.rmtree(home_path+path)  # remove dir and all contains	
	
	
	
	if x == '2':
		arq = open(home_path + path, 'w') 
		while 1:
			dados = con.recv(1024)
			if not dados:
				break
			arq.write(dados)
			arq.close()
	if x == '5':
		path1 = msg2[2]
		print 'comando '+ x + path + path1
		if os.path.isfile(home_path + path) and os.path.isdir(home_path+path1):
			shutil.copy(home_path + "/" + path, home_path+path1)		
		
tcp.close()

