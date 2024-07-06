import socket

sock2 = socket.socket()

sock2.connect(('127.0.0.1', 9999))

print("Socket Connected")

while True:
    str = sock2.recv(102400).decode('utf-8')
    print(str)

    sock2.send(("接受到你的消息啦:" + str).encode('utf-8'))