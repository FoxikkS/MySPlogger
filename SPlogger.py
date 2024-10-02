import logging
import coloredlogs

class SPLogger(logging.Logger):
    def __init__(self, name='SPLogger', level='INFO', fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'):
        super(SPLogger, self).__init__(name, level)
        coloredlogs.install(
            logger=self,
            level=level,
            fmt=fmt,
            datefmt=datefmt
        )

    def log(self, level, msg, *args, **kwargs):
        super(SPLogger, self).log(level, msg, *args, **kwargs)

logger_instance = SPLogger()

def SPinfo(message, level='INFO'):
    logger_instance.log(getattr(logging, level.upper()), message)