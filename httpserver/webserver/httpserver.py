# coding=utf-8
"""
主程序
"""


from socket import *
from threading import Thread
from config import *
import re
import json


# 和后端应用程序交互
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except Exception as e:
        print(e)
        return
    # 将字典发送给web frame
    data = json.dumps(env, separators=(',', ':'))
    s.send(data.encode())
    # 等待后端应用的数据回复
    try:
        data = s.recv(1024 * 1024 * 10).decode()
        return json.loads(data)
    except:
        return


class HTTPServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.address = (HOST, PORT)
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d..." % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print("Connect from browser", addr)
            # 为每个新的客户端单独创建一个线程处理
            t = Thread(target=self.handle, args=(connfd,))
            t.setDaemon(True)
            t.start()

    # 具体处理客户端（浏览器）请求
    def handle(self, connfd):
        request = connfd.recv(4096).decode()
        # print(request)
        # 从请求中提取请求类型和请求内容
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            data = connect_frame(env)
            if data:
                self.response(connfd, data)  # 组织响应

    def response(self, connfd, data):
        # data --> {'status':'200',data:'xxxx'}
        if data['status'] == '200':
            responseHeader = "HTTP/1.1 200 OK\r\n"
            responseHeader += "Content-Type:text/html\r\n"
            responseHeader += "\r\n"
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeader = "HTTP/1.1 404 Not Found\r\n"
            # responseHeader += "Content-Type:text/html\r\n"
            responseHeader += "Content-Type:application/json\r\n"
            responseHeader += "\r\n"
            responseBody = data['data']
        # 将数据发送给浏览器
        response_data = responseHeader + responseBody
        connfd.send(response_data.encode(encoding="utf-8"))


if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve_forever()  # 启动服务
