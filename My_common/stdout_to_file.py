# encoding=utf-8
import sys
import os
import logbook
import logbook.more


def log_format(record, handle):
    layout = "[{date}] {msg}".format(
        date=record.time,  # 日志时间
        msg=record.message  # 日志内容
    )
    return layout


def init_logger(record_dispatcher):
    logbook.set_datetime_format('local')
    log_obj = logbook.Logger(record_dispatcher)
    log_obj.handlers = []
    # 日志输出到文件
    log_file = logbook.TimedRotatingFileHandler(os.path.join(r"D:\python\log", '%s.log' % record_dispatcher),
                                                date_format='%Y_%m_%d',
                                                bubble=True, encoding='utf-8')
    log_file.formatter = log_format
    log_obj.handlers.append(log_file)
    return log_obj


class StdoutToFile:

    def __init__(self,run_file_name):
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self.local_file_name = run_file_name
        sys.stdout = self
        sys.stderr = self

    def write(self, info):
        # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
        module_name = 'my_log2'
        logger = init_logger(module_name)
        if info.startswith("  File") and self.local_file_name in info:
            info = info.strip()
            logger.debug(info)
        self.stdout.write('\033[1;31;3m' + info + '\033[0m')

    def restore_std(self):
        # 准备恢复标准输出
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        # 恢复标准输出完成

    def __del__(self):
        self.restore_std()

    def flush(self):
        pass


StdoutToFile(__file__)
wi
