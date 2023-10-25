import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(1)

print("Сервер слухає на порті %s..." % server_address[1])

client_socket, client_address = server_socket.accept()
print("З'єднання встановлене з адреси: %s" % str(client_address))

while True:
    # Отримання повідомлення від клієнта
    message = client_socket.recv(1024).decode('utf-8')
    print("Повідомлення від клієнта: %s" % message)

    # Обробка отриманого повідомлення (тут можна вставити логіку обробки)


    # Відправлення відповіді клієнту
    response = "Отримав повідомлення: %s" % message
    client_socket.send(response.encode('utf-8'))

# Закриття з'єднання
client_socket.close()
server_socket.close()
