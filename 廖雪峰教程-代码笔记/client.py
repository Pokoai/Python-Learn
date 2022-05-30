import socket,threading,random

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s.bind(('192.168.1.6',random.randint(10038,10050)))

user=input('请输入昵称')

ser_addr=('81.68.198.46',10028)

msg=''

def send_msg():     # 发消息

    while True:

        msg = input('')

        s.sendto(('%s:%s' % (user, msg)).encode('utf-8'), ser_addr)

def recv_msg():   # 刷新聊天室消息

    while True:

        print(s.recv(1024).decode('utf-8'))

send_msg=threading.Thread(target=send_msg)     # 发消息线程

recv_msg=threading.Thread(target=recv_msg)      # 刷新聊天室线程

send_msg.start()

recv_msg.start()