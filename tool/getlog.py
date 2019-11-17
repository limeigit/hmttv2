import logging.handlers


class GetLog:
    logger = None

    # 定义获取日志的方法
    @classmethod
    def get_log(cls):
        if cls.logger is None:
            # 1.创建日志器对象
            logger = logging.getLogger()
            # 2.创建处理器
            handle_info = logging.handlers.TimedRotatingFileHandler(filename="./log/info.log", when="h",
                                                                    backupCount=3)
            handle_error = logging.handlers.TimedRotatingFileHandler(filename="./log/error.log", when="h",
                                                                     backupCount=3)
            # 3.建立格式化器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            formatter = logging.Formatter(fmt)
            # 4.将格式器添加处理器
            handle_info.setFormatter(formatter)
            handle_error.setFormatter(formatter)
            # 5.将处理器添加到日志器
            logger.addHandler(handle_info)
            logger.addHandler(handle_error)
        return cls.logger
