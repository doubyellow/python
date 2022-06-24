# coding=utf-8
import re


def get_function_name(file_path):
    function_list = list()
    with open(file_path, "r", encoding='utf-8') as f:
        while True:
            res = f.readline()
            if not res:
                break
            func = re.findall(r"def (.*?)\(", res)
            if func:
                function_list.extend(func)
        return function_list


