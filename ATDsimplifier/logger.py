import logging


if __name__ == "logger":
    file_log = logging.FileHandler('simplifier.log')
    console_out = logging.StreamHandler()
    log_handlers = (file_log, console_out)
    logging.basicConfig(handlers=log_handlers,
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S', level=logging.DEBUG)
else:
    logging.basicConfig(filename='simplifier.log', filemode='w',
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S', level=logging.DEBUG)


log = logging.getLogger(__name__)
