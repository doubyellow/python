def __headers_generator(file_path):
    try:
        with open(file_path, encoding="utf-8") as f:
            while True:
                data = f.readline()
                if not data:
                    break
                yield data
    except Exception as e:
        print(str(e))


def headers_data(file):
    _dict = dict()
    for line in __headers_generator(file):
        data = line.split(":")
        _dict[data[0].strip()] = data[-1].strip()
    return _dict


class HeadersHandle:
    def __init__(self, file_path):
        self.file_path = file_path


