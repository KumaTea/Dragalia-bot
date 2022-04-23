import botCache
from data import groups
from session import dra
from datetime import datetime
from data import timer_sticker


def timer():
    now = datetime.now()
    ts = datetime.timestamp(now)

    for group in groups:
        lang = groups[group]['lang']
        try:
            if ts - botCache.last_msg_time[group] > 3600:
                hour = int(now.strftime('%I'))
                sticker = timer_sticker[lang][hour]
                dra.send_sticker(group, sticker)
        except:
            pass
    return True
