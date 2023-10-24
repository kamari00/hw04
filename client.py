import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)


while True:
    # Введення повідомлення для відправлення серверу
    message = input("Введіть повідомлення: ")

    # Відправлення повідомлення серверу
    client_socket.send(message.encode('utf-8'))

    # Отримання відповіді від сервера
    response = client_socket.recv(1024).decode('utf-8')
    print("Відповідь від сервера: %s" % response)

# Закриття з'єднання
client_socket.close()
