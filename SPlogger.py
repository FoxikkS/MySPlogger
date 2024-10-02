import logging
import coloredlogs

class SPLogger(logging.Logger):
    def __init__(self, name='SPLogger', level='INFO', fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'):
        super(SPLogger, self).__init__(name, level)
        coloredlogs.install(
            logger=self,
            level=self.level,
            fmt=fmt,
            datefmt=datefmt
        )

logger_instance = SPLogger()

def SPinfo(message):
    logger_instance.info(message)
