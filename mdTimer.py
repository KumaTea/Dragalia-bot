import botCache
from botSession import dra
from datetime import datetime
from botDB import timer_sticker
from botInfo import player_group


def timer():
    now = datetime.now()
    ts = datetime.timestamp(now)

    if ts - botCache.last_msg_time < 3600:
        return None

    hour = int(now.strftime('%I'))
    sticker = timer_sticker[hour]
    return dra.send_sticker(player_group, sticker)
