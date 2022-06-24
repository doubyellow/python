# coding=utf-8
import tkinter
# 导入filedialog
from tkinter import filedialog


def txt_read_line():
    windows = tkinter.Tk()
    # 隐藏窗口
    windows.withdraw()
    # 获取文件路径
    file_path = filedialog.askopenfilename(title='打开单个文件', filetypes=[('文本文件', '*.txt')],
                                           # 只处理的文件类型
                                           initialdir=r'C:\Users\ASUS\Desktop\data')
    try:
        with open(file_path, encoding="utf-8") as f:
            while True:
                data = f.readline()
                if not data:
                    break
                yield data
    except Exception as e:
        print(str(e))
        pass


if __name__ == '__main__':
    for line in txt_read_line():
        print(line)
