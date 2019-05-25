from dataio import getchatid, getmsg, sendmsg, getmsgid, editmsg, getreply, delmsg, getusrinfo, codetolang
from mddebug import mddebug
from mdfunc import dracal
from threading import Timer


def mdgrpcmd(data):
    chatid = getchatid(data)
    command = getmsg(data)
    msgid = getmsgid(data)
    langcode = getusrinfo(data, 'language')
    language = codetolang(langcode)

    if command.startswith(('/cal', '/日历', '/カレ')):
        calmsg = dracal(language)
        resp = sendmsg(chatid, calmsg, msgid)
        calid = getmsgid(resp)
        delcal = Timer(3600, editmsg, [chatid, calid, 'Outdated /calendar message'])
        delcal.start()
        return resp

    elif command.startswith('/debug'):
        cont = command.find(' ')
        if cont == -1:
            resp = mddebug(data)
        else:
            resp = mddebug(data, True)
        return resp

    else:
        return 'Pass in group'
