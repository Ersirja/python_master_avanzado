import socket

host = socket.gethostname()
port= 12345 #nombre del servidor
mensaje = "hola mundito" # tamaño de ficheros que pueden entrar
#el socket con el with es muy seguro


with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as socket_tcp:
    socket_tcp.connect((host,port))
    print("enviando mensaje...")
    socket_tcp.send((mensaje.encode('utf-8')))

    data = socket_tcp.recv(1024)
    print("Datos recibidos: {}".format(data.decode('utf-8')))  # mostramos datos
