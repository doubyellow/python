# coding=utf-8
import json


def beauty_json(file):
    with open(file) as f:
        data = json.load(fp=f)
    try:
        data = json.dumps(data, sort_keys=True, indent=2)
        print(data)
    except Exception as e:
        print(e)
    with open(file, "w") as f:
        f.write(data.encode('utf-8').decode('unicode_escape'))
        print(data.encode('utf-8').decode('unicode_escape'))
    return data.encode('utf-8').decode('unicode_escape')


if __name__ == '__main__':
    file1 = r"D:\python\中电惠融\企业端\签发管理\签发申请\新增签发\payload.txt"
    beauty_json(file1)
