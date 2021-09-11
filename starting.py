# import botCache
# from botDB import groups
from botTools import mkdir
from botSession import dra, logger, scheduler
from register import register_handlers, manager


def starting():
    mkdir(['tmp', 'life'])
    # for group in groups:
    #     botCache.last_msg_time[group] = 0
    register_handlers()
    manager()
    scheduler.start()
    logger.warning('Starting fine.')
