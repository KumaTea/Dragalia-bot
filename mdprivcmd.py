from dataio import getchatid, getmsg, getusrinfo, sendmsg, localization, codetolang
from mddebug import mddebug
from mdfunc import dracal
import botdb


def mdprivcmd(data):
    chatid = getchatid(data)
    command = getmsg(data)
    langcode = getusrinfo(data, 'language')
    language = codetolang(langcode)

    if command.startswith('/start'):
        localmsg = localization(botdb.hellomsg, langcode)
        resp = sendmsg(chatid, localmsg)
        return resp

    elif command.startswith('/help'):
        localmsg = localization(botdb.helpmsg, langcode)
        resp = sendmsg(chatid, localmsg)
        return resp

    elif command.startswith(('/cal', '/日历', '/カレ')):
        calmsg = dracal(language)
        resp = sendmsg(chatid, calmsg)
        return resp

    elif command.startswith('/debug'):
        cont = command.find(' ')
        if cont == -1:
            resp = mddebug(data)
        else:
            resp = mddebug(data, True)
        return resp

    else:
        localmsg = localization(botdb.cmderror, langcode)
        resp = sendmsg(chatid, localmsg)
        return resp
