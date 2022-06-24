import os, time, logging

path = os.getcwd()


class Logger:
    def __init__(self, title: str = None, module_name: str = 'my_logging'):  # Eg: title = u'注册测试'
        day = time.strftime("%Y_%m_%d", time.localtime(time.time()))
        file_dir = r'D:\python\log'
        file = os.path.join(file_dir, (module_name + '-' + day + '.log'))
        # 创建日志标题
        self.title = title
        # 创建日志对象
        self.logger = logging.Logger(title)
        # 创建日志级别
        self.logger.setLevel(logging.INFO)
        # 创建handler对象
        self.handler = logging.FileHandler(file)
        # 设置录制级别
        self.handler.setLevel(logging.INFO)

        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)

        # self.fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fmt = logging.Formatter("[%(asctime)s] - %(filename)s[%(lineno)d] - %(levelname)s;  %(message)s")

        self.handler.setFormatter(self.fmt)
        # self.control.setFormatter(self.fmt)

        self.logger.addHandler(self.handler)
        # self.logger.addHandler(self.control)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


if __name__ == '__main__':
    logger = Logger("functionName")
    # logger.debug("this is debug") # 文件中不显示
    logger.info('this is info')
    logger.warning("this is warning")
    logger.error("this is error")
