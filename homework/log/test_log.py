from test_appium.homework.log import alog
from test_appium.homework.log.alog import ALog

a=ALog().get_logger()
a.debug("debug message")
a.info("info message")
a.warning("warning message")
a.error("error message")
a.critical("critical message")