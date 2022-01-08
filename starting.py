# import botCache
# from botDB import groups
import logging
from botTools import mkdir
from botSession import scheduler
from register import register_handlers, manager


def starting():
    mkdir(['tmp', 'life'])
    # for group in groups:
    #     botCache.last_msg_time[group] = 0
    register_handlers()
    manager()
    scheduler.start()
    logging.warning('Starting fine.')
