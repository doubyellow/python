import logging
import time
import os

# 设置日志文件保存路径
day = time.strftime("%Y_%m_%d", time.localtime(time.time()))
file_dir = r'/log'
file = os.path.join(file_dir, (day + '.log'))

# 日志对象
logger = logging.getLogger()
# 日志级别
logger.setLevel(level=logging.ERROR)
""" _nameToLevel = {
    'CRITICAL': CRITICAL, #极重要的
    'FATAL': FATAL,  # 致命的 
    'ERROR': ERROR,
    'WARN': WARNING, # 警告
    'WARNING': WARNING, # 警告
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
}
"""
# 创建 handler 对象
handler = logging.FileHandler(file)

# 发生 logging.ERROR 就写入文件
handler.setLevel(logging.INFO)

# handler 信息写入格式
fmt = logging.Formatter("%(asctime)s - %(module)s - %(filename)s[%(lineno)d] -%(levelname)s-%(funcName)s;  %(message)s")

""" %(name)s            Name of the logger (logging channel)
    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                        WARNING, ERROR, CRITICAL)
    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        Full pathname of the source file where the logging
                        call was issued (if available)
    %(filename)s        Filename portion of pathname
    %(module)s          Module (name portion of filename)
    %(lineno)d          Source line number where the logging call was issued
                        (if available)
    %(funcName)s        Function name
    %(created)f         Time when the LogRecord was created (time.time()
                        return value)
    %(asctime)s         Textual time when the LogRecord was created
    %(msecs)d           Millisecond portion of the creation time
    %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                        relative to the time the logging module was loaded
                        (typically at application startup time)
    %(thread)d          Thread ID (if available)
    %(threadName)s      Thread name (if available)
    %(process)d         Process ID (if available)
    %(message)s         The result of record.getMessage(), computed just as
                        the record is emitted
"""
# handler 设置写入格式
handler.setFormatter(fmt)

# logger 对象添加 handler
logger.addHandler(handler)


def test_logger():
    try:
        int("123_c123")
    except Exception as e:
        logger.error(str(e))


if __name__ == '__main__':
    test_logger()
