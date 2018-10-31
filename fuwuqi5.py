# -*- coding: UTF-8 -*-
import socket
name=socket.gethostname()
port=2000
s=socket.socket()
s.bind((name,port))
s.listen(3)
print('(1)接收或发送over0断开连接并连接下一个客户端\n(2)关闭客户端界面直接退出循环\n\
(3)接收或发送shou1进入接收信息状态(默认状态)\n(4)接收fan2进入接收并返回信息状态\n\
(5)接收或发送song3进入发送状态\n(6)消息日志保存在store.txt文件中(结束进程后自动生成)\n')

def shou(file):
    print('收到的消息为:',file)

def song(file):
    file='服务端发送:'+str(file)+'\n'
    return data.send(bytes(file, encoding = "utf8"))

def fan(file):
    file='服务端返回:'+str(file)+'\n'
    return data.send(bytes(file, encoding = "utf8"))

def xie(file,mode):
    if mode==1:
        return '收到的消息为:'+str(file)
    elif mode==2:
        return '返回的消息为:'+str(file)
    elif mode==3:
        return '发送的消息为:'+str(file)

def cun(a):
    f=open('store.txt','a+')
    f.write(str(a)+'\n')
    f.close()

print('等待连接中......')
while 1:
    data,addr=s.accept()  
    a=print('已连接上:',addr)
    b=1
    song('hello')
    cun(addr)
    while 1:  
        if b==1 or b==2:
            r=data.recv(1024)        
        if r==b'over0':
            break
        elif r==b'shou1':
            b=1
        elif r==b'fan2':
            b=2
        elif r==b'song3':
            b=3
        
        if b==1:
            m=r.decode("utf-8")
            print('接收状态:')
            shou(m)       
            cun(xie(m,b))
        elif b==2:
            m=r.decode("utf-8")
            print('返回状态:')
            shou(m)
            fan(m)
            cun(xie(m,b))
        elif b==3:
            print('发送状态:')
            a=input("回复:")
            song(a)
            cun(xie(a,b))
            if a=='shou1':
                b=1
                print('已进入接收状态')
            elif a=='fan2':
                b=2
                print('已进入返回状态')
            elif a=='over0':
                break