import json
from dataio import sendmsg, sendfile
from starting import getadminid


def mddebug(data, log=False):
    adminid = getadminid()
    debugmsg = json.dumps(data)
    sendmsg(adminid, debugmsg)
    if log:
        sendfile(adminid, 'log/log.csv', False, 'upload')
    """
    if os.name == 'nt':
        scrst = scrshot.grab()
        scrst.save('log/screenshot.png')
        sendphoto(adminid, 'log/screenshot.png', False, 'upload')
    """
    return 'DEBUG FINISHED'
