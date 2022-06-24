# coding=utf-8
import hashlib
import multiprocessing


def func1(func, string1, string2):
    a = func()
    a.update(string1.encode('utf-8'))
    res = a.hexdigest()
    if string2 in res:
        print(str(func))
    print(res)


func_set = {
    hashlib.md5,
    hashlib.sha1,
    hashlib.sha224,
    hashlib.sha256,
    hashlib.sha384,
    hashlib.sha512,
    hashlib.sha3_224,
    hashlib.sha3_256,
    hashlib.sha3_384,
    hashlib.sha3_512,
}

if __name__ == '__main__':
    string = "9B2GGY"
    string_end = "852bd7f41304091c5d3843f3658f6"
    lst_task = []
    for item in func_set:
        p = multiprocessing.Process(target=func1, args=(item, string, string_end))
        lst_task.append(p)
        p.start()
    for p in lst_task:
        p.join()
