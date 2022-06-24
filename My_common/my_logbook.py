# coding=utf-8
import os
import logbook
import logbook.more


class Logger:

    def __init__(self, module_name: str = "my_logbook"):
        self.module_name = module_name
        self.file_path = os.path.join(r"D:\python\log", '%s.log' % self.module_name)

    @staticmethod
    def log_format(record, handle):
        layout = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
            date=record.time,  # 日志时间
            level=record.level_name,  # 日志等级
            filename=os.path.split(record.filename)[-1],  # 文件名
            func_name=record.func_name,  # 函数名
            lineno=record.lineno,  # 行号
            msg=record.message  # 日志内容
        )
        return layout

    def init_logger(self, fileout=True, stdout=False):
        # 设置时间格式
        logbook.set_datetime_format('local')
        # 创建logger对象
        log_obj = logbook.Logger(self.module_name)
        # 创建handlers对象
        log_obj.handlers = []

        # 日志输出到指定文件
        if fileout:
            log_file = logbook.TimedRotatingFileHandler(self.file_path, date_format='%Y_%m_%d', bubble=True,
                                                        encoding='utf-8')
            # 设置日志输入格式
            log_file.formatter = Logger.log_format
            # 处理日志文件对象
            log_obj.handlers.append(log_file)

        # 日志打印到屏幕
        if stdout:
            log_std = logbook.more.ColorizedStderrHandler(bubble=True)
            # 设置日志输入格式
            log_std.formatter = Logger.log_format
            # 处理日志文件对象
            log_obj.handlers.append(log_std)
        return log_obj


if __name__ == '__main__':
    logger = Logger().init_logger(fileout=True)
    logger.info('this is info')
    logger.warning("this is warning")
    logger.debug("this is debug")
    logger.critical("this is critical")
