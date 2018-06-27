"""
Log uncaught exceptions using sys.excepthook
"""
import logging
import sys
import traceback

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(levelname)s:%(name)s:%(pathname)s:%(lineno)d:%(message)s")


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    # To format exception on one line
    # logging.critical("Uncaught exception:%s", traceback.format_exception(
    #     exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception

cause['NameError']
