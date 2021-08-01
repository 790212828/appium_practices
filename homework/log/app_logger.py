import datetime
import logging
import logging.handlers


class AppLogger:
    def get_logger(self):
        self.logger=logging.getLogger('mylogger')
        self.logger.setLevel(logging.DEBUG)
        self.rf_handler=logging.handlers.TimedRotatingFileHandler("../log/all.log",when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
        self.rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

        self.f_handler=logging.FileHandler('../log/error.log')
        self.f_handler.setLevel(logging.ERROR)
        self.f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s"))

        self.logger.addHandler(self.rf_handler)
        self.logger.addHandler(self.f_handler)

        return self.logger