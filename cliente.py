import socket
HOST = '127.0.0.1'
PORT = 8001 
tcp =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST,PORT))
msg = raw_input("digite algo: ")
tcp.send(msg)
tcp.close()
