from decorators import log
import logging


class Model():
    @log.logger(logging.DEBUG, "Creating model attributes", "model")
    def __init__(self, document):
        try:
            for k, v in document.items():
                setattr(self, k, v)
        except:
            pass
