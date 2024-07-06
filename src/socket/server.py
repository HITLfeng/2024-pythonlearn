import random
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 9999))
sock.listen()

print("Socket is listening...")
conn, addr = sock.accept()
print(conn.getsockname())

print("address is ", addr)
while True:
    # conn.send(b'Hello World!')
    conn.send(("wujia航" + str(random.randint(1, 100))).encode('utf-8'))
    # str = conn.recv(1024).decode('utf-8')
    # print("str is " + str)
