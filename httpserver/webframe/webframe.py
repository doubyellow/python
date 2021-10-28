"""
模拟实现后端应用
"""

from socket import *
import json
from settings import *
from threading import Thread
from urls import *


# 处理请求
class Application(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def get_html(self, info):
        if info == '/' or info == '/favicon.ico':
            filename = STATIC + "/index.html"
        else:
            filename = STATIC + info
        try:
            with open(filename, encoding='utf-8') as f:
                data = f.read()
            # fd = open(filename)
            status = "200"
        except:
            with open(STATIC + '/404.html', encoding='utf-8') as f:
                data = f.read()
            # fd = open(STATIC + '/404.html')
            status = "404"
        return {'status': status, 'data': data}

    # 处理非网页情况
    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
            else:
                # with open(STATIC + '/404.html', encoding='utf-8') as f:
                #     data = f.read()
                # return {'status': '404', 'data': data}
                return {'status': '404', 'data': 'Sorry...'}

    # 执行线程功能
    def run(self):
        # 接收请求 {‘method’：‘GET’,'info':'xxxxx'}
        request = self.connfd.recv(1024).decode()
        request = json.loads(request)  # 转换为Python字典
        print("request:", request)
        if request['method'] == 'GET':
            # 根据情况调用函数，返回值即得到的数据 --》{}
            info = request.get("info", "/")
            if info == '/' or info[-5:] == ".html" or not info or info == '/favicon.ico':
                response = self.get_html(info)
            else:
                response = self.get_data(info)
        elif request['method'] == 'POST':
            pass
        # 将数据发送给httpserver
        response = json.dumps(response)
        self.connfd.send(response.encode())
        self.connfd.close()


# 搭建网络模型
def main():
    # 套接字创建
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((frame_ip, frame_port))
    s.listen(3)
    print("Listen the port 8800")
    while True:
        c, addr = s.accept()
        print("Connect from httpserver", addr)

        # 创建线程
        app = Application(c)
        app.setDaemon(True)
        app.start()


if __name__ == '__main__':
    main()
