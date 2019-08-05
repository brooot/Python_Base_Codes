 from socket import *
import sys
import os

address = './sockfile'
#确保在使用sockfiler前，这个文件是不存在的
try:
    os.unlink(address)
except OSError:
    if os.path.exists(address):
        raise
sockfd = socket(AF_UNIX,SOCK_STREAM)
sockfd.bind(address)
sockfd.listen(5)

while True:
    conn,addr=sockfd.accept()
    print('connect from',addr)
    while True:
        data = conn.recv(1024).decode()
        print('recv',data)
        if not data:
            break
        conn.send('recv your message'.encode())
    conn.close()
sockfd.close()
