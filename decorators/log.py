from functools import wraps
import logging


def logger(level, message=None, name=None):
    def decorate(func):
        logname = name if name else func.__module__
        logging.basicConfig(level=level)
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate
