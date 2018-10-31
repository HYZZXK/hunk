# -*- coding: UTF-8 -*-
import socket
name=socket.gethostname()
s=socket.socket()
s.connect((name,2000))
print('(1)输入gets接收消息\n(2)输入over0断开连接\n')
def song(file):
    return s.send(bytes(file, encoding = "utf8"))

def shou():
    a=(s.recv(1024)).decode("utf-8")
    print(a)

while 1:
    m=input("输入:")
    if m=='shou':
       shou() 
    else:
       song(m)       
     