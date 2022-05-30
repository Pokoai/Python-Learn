# server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM 指定了这个 Socket 的类型是 UDP
s.bind(('127.0.0.1', 8999))

# 绑定端口和 TCP 一样，但是不需要调用 listen() 方法，
# 而是直接接收来自任何客户端的数据：

print('Bind UDP on 9999...')
while True:
    # 接受数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello, %s!' % data, addr)

# recvfrom()方法返回数据和客户端的地址与端口，
# 这样，服务器收到数据后，直接调用 sendto()就可以把数据用 UDP 发给客户端。