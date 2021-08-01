import datetime
import logging
import logging.handlers


class ALog:
    def get_logger(self):
        logger=logging.getLogger('mylogger')
        logger.setLevel(logging.DEBUG)
        rf_handler=logging.handlers.TimedRotatingFileHandler("all.log",when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
        rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

        f_handler=logging.FileHandler('error.log')
        f_handler.setLevel(logging.ERROR)
        f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s"))

        logger.addHandler(rf_handler)
        logger.addHandler(f_handler)

        return logger

# logger=logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
# rf_handler=logging.handlers.TimedRotatingFileHandler("all.log",when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
# rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))
#
# f_handler=logging.FileHandler('error.log')
# f_handler.setLevel(logging.ERROR)
# f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s"))
#
# logger.addHandler(rf_handler)
# logger.addHandler(f_handler)

# if __name__ == '__main__':
#     # logger.debug("debug message")
#     # logger.info("info message")
#     # logger.warning("warning message")
#     # logger.error("error message")
#     # logger.critical("critical message")


#     a=ALog().get_logger()
#     a.debug("debug message")
#     a.info("info message")
#     a.warning("warning message")
#     a.error("error message")
#     a.critical("critical message")








