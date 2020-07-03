import os
import botCache
from botDB import groups
from botSession import dra, logger, scheduler
from register import register_handlers, manager
try:
    from localDB import frp_url
except ImportError:
    frp_url = ''


def set_frp(url, path=None):
    return dra.set_webhook(url, path)


def mkdir(folder=None):
    if not os.path.exists('../vote'):
        os.mkdir('../vote')
    if folder:
        if type(folder) == list or type(folder) == tuple:
            for items in folder:
                if not os.path.exists(str(items)):
                    os.mkdir(str(items))
        else:
            if not os.path.exists(str(folder)):
                os.mkdir(str(folder))


def starting():
    mkdir(['tmp', 'life'])
    # set_frp(frp_url)
    for group in groups:
        botCache.last_msg_time[group] = 0
    register_handlers()
    manager()
    scheduler.start()
    logger.warn('Starting fine.')  # It's actually an info
