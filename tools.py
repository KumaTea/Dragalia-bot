import os
from data import groups, lang_code


def mkdir(folder=None):
    if folder:
        if type(folder) == list or type(folder) == tuple:
            for items in folder:
                if not os.path.exists(str(items)):
                    os.mkdir(str(items))
        else:
            if not os.path.exists(str(folder)):
                os.mkdir(str(folder))


def detect_lang(message):
    lang = None
    chat_id = message.chat.id
    user_lang = message.from_user.language_code
    if user_lang and 'zh' in user_lang.lower():
        for i in lang_code:
            for j in lang_code[i]:
                if j in user_lang.lower():
                    lang = i
                    break
    if not lang:
        if chat_id in groups:
            lang = groups[chat_id]['lang']
        else:
            lang = 'chs'
    return lang
