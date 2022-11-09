import socket

host = socket.gethostname()
port = 12345
BUFFER_SIZE = 1024
# tamaño de ficheros que pueden entrar
#el socket con el with es muy seguro

# my_socket= socket.socket(socket_family,socket_type,protocol=0)
# socket_family=protocolo que se usa como transporte AF_INET, PF_INET, PF_UNIX, PF_X25, entre otros
# socket_type tipo de comunicación entre ambos extremos de la conexión SOCK_STREAM para protocolos orientados a conexiones y SOCK_DGRAM para protocolos sin conexiones
# protocol = normalmente es 0, es utilizado apra identificar la variante de un protocolo dentro de una familia y tipo
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port))  # vincula un host con un port
    socket_tcp.listen(5)  # esta a la espera de que llegue un cliente
    con, addr = socket_tcp.accept()  # establecemos conexión
    with con:
        print("Conexión establecida")
        while True:
            data = con.recv(BUFFER_SIZE)  # recibimos paquete en bytes y hay que convertilo a str
            if not data:
                break
            else:
                print("Datos recibidos: {}".format(data.decode('utf-8')))  # mostramos datos

