from dataio import getchatid, getmsg, getusrinfo, sendmsg, localization, codetolang
from mdprivcmd import mdprivcmd
from botdb import priverror


def privtext(data):
    msg = getmsg(data)
    if msg.startswith('/'):
        resp = mdprivcmd(data)
        return resp
    else:
        chatid = getchatid(data)
        langcode = getusrinfo(data, 'language')
        language = codetolang(langcode)
        localmsg = localization(priverror, language)
        resp = sendmsg(chatid, localmsg)
        return resp


def privsticker(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    sticker = getfileid(data)
    resp = sendsticker(chatid, sticker)
    return resp
    """
    return 'Sticker. Function not enabled'


def privphoto(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    photo = getfileid(data)
    resp = sendphoto(chatid, photo)
    return resp
    """
    return 'Photo. Function not enabled'


def privvideo(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    video = getfileid(data)
    resp = sendvideo(chatid, video)
    return resp
    """
    return 'Video. Function not enabled'


def privfile(data):
    """Uncomment when enable this function
    chatid = getchatid(data)
    file = getfileid(data)
    resp = sendfile(chatid, file)
    return resp
    """
    return 'File. Function not enabled'
