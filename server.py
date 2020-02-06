import socket
import time  
# Задаем адрес сервера
SERVER_ADDRESS = ('localhost', 8686)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')


# Слушаем запросы
while True:
    time.sleep(5)
    connection, address = server_socket.accept()
    print("New connection from {address}".format(address=address))

    data = connection.recv(1024)
    udata = data.decode('utf-8', "ignore")
    print(udata)

    connection.close()
