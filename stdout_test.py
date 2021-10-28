# encoding=utf-8
import sys


class MyStdout:
    def __init__(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def write(self, info):
        # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
        # str_info = info.rstrip("\n")
        # str_info = info.split('\n')[0]
        str_info = info
        if len(str_info):
            self.process_info('\033[1;31;3m' + str_info + '\033[0m')  # 对输出信息进行处理的方法

    def process_info(self, info):
        self.stdout.write(info)  # 可以将信息再输出到原有标准输出，在定位问题时比较有用

    def restore_std(self):
        # print("准备恢复标准输出")
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        # print("恢复标准输出完成")

    def __del__(self):
        self.restore_std()

    def flush(self):
        pass


# print("主程序开始运行,创建标准输出替代对象....")
my_stdout = MyStdout()
# print("标准输出替代对象创建完成,准备销毁该替代对象")


