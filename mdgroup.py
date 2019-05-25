from dataio import getchatid, getmsgid, getmsg, getusrinfo, sendmsg, localization, codetolang
from mdgrpcmd import mdgrpcmd
from botdb import grperror


def grpnewmem(data):
    """Uncomment when enable this function
    if not data['message']['new_chat_member']['is_bot']:
        groupid = getchatid(data)
        if grpwelcome.get(groupid) is not None:
            if grpwelcome[groupid].get('message') is not None:
                resp = sendmsg(groupid, grpwelcome[groupid]['message'])
            if grpwelcome[groupid].get('sticker') is not None:
                resp = sendsticker(groupid, grpwelcome[groupid]['sticker'])
        return resp
    else:
        return 'Passed in unfamiliar group'
    """
    return 'New member. Welcome not enabled'


def grptext(data):
    msg = getmsg(data)
    if msg.startswith('/'):
        resp = mdgrpcmd(data)
        return resp
    else:
        chatid = getchatid(data)
        msgid = getmsgid(data)
        langcode = getusrinfo(data, 'language')
        language = codetolang(langcode)
        localmsg = localization(grperror, language)
        resp = sendmsg(chatid, localmsg, msgid)
        return resp


def grpsticker(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    sticker = getfileid(data)
    msgid = getmsgid(data)
    resp = sendsticker(chatid, sticker, msgid)
    return resp
    """
    return 'Sticker. Function not enabled'


def grpphoto(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    photo = getfileid(data)
    msgid = getmsgid(data)
    resp = sendphoto(chatid, photo, msgid)
    return resp
    """
    return 'Photo. Function not enabled'


def grpvideo(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    video = getfileid(data)
    msgid = getmsgid(data)
    resp = sendvideo(chatid, video, msgid)
    return resp
    """
    return 'Video. Function not enabled'


def grpfile(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    file = getfileid(data)
    msgid = getmsgid(data)
    resp = sendfile(chatid, file, msgid)
    return resp
    """
    return 'File. Function not enabled'
