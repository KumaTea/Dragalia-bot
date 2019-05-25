import dragaliadb
import botdb
import pytz
from datetime import datetime


def timelocalize(rawtime, language):
    year = rawtime.strftime('%Y')
    month = rawtime.strftime('%m')
    day = rawtime.strftime('%d')
    hour = rawtime.strftime('%H')
    minute = rawtime.strftime('%M')
    rawweek = datetime.weekday(rawtime)
    for lang in botdb.langlist:
        if lang in language:  # if 'Hans' in 'zh-Hans'
            code = botdb.langdict[lang]
            weekday = dragaliadb.timelocal['dayofweek'][code][rawweek]
            if code == 'en':
                enmonth = rawtime.strftime('%b')
                lctime = weekday + ', ' + enmonth + ' ' + day + ', ' + year + ' ' + hour + ':' + minute
                return lctime
            else:
                lctime = year + '年' + month + '月' + day + '日' + weekday + ' ' + hour + ':' + minute
                return lctime
    weekday = dragaliadb.timelocal['dayofweek']['en'][rawweek]
    enmonth = dragaliadb.timelocal['month']['en']
    lctime = weekday + ', ' + enmonth + ' ' + day + ', ' + year + ' ' + hour + ':' + minute
    return lctime


def dracal(language):
    rawtime = datetime.now(pytz.timezone('America/Denver'))
    rawweek = datetime.weekday(rawtime)
    lctime = timelocalize(rawtime, language)
    calmsg = dragaliadb.dracalendar[language].format(lctime, dragaliadb.ruins[rawweek]['symbol'], dragaliadb.void[rawweek]['symbol'])
    return calmsg
