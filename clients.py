import socket
HOST = '127.0.0.1'
PORT = 8002
tcp =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST,PORT))
x = 10
while (x > 0):
    print ("Digite 1 para criar uma pasta")  
    print ("Digite 2 para adicionar arquivos na pasta") 
    print ("Digite 3 para remover arquivos da pasta") 
    print ("Digite 4 para remover a pasta") 
    print ("Digite 5 para copiar um arquivo para uma pasta")
    x = raw_input("Digite um comando: ")
    if x == '5':
        path = raw_input('Digite o nome do arquivo: ') 
        path1 = raw_input('Digite a pasta de destino do arquivo: ')
        msg = x + '.' + path + '.' + path1   
        tcp.send(msg)
    elif x == '2':
        tcp.send(x)
        path = raw_input('Digite o nome do arquivo: ')
        arq = open(path, 'r')
        for i in arq.readlines():
            tcp.send(i)
        arq.close()
    else:
        path = raw_input('Digite nome + extensao: ')
        msg = x + '.' + path
        tcp.send(msg)
    
    
    
tcp.close()