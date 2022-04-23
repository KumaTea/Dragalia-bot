from data import *
from session import dra
from info import developer_id
from tools import detect_lang
from datetime import datetime, timezone, timedelta


def send_time(client, message):
    
    chat_id = message.chat.id

    now = datetime.now(timezone(timedelta(hours=8)))
    lang = detect_lang(message)
    hour = int(now.strftime('%I'))
    sticker = timer_sticker[lang][hour]
    return dra.send_sticker(chat_id, sticker)


def private_start(client, message):
    return message.reply(start_message)


def private_help(client, message):
    return message.reply(help_message)


def help_english(client, message):
    return message.reply(help_en)


def help_japanese(client, message):
    return message.reply(help_ja)


def private_get_file_id(client, message):
    file_id = 'Unknown type of media.'
    if message.text:
        file_id = message.text
    elif message.sticker:
        file_id = message.sticker.file_id
    elif message.photo:
        file_id = message.photo[-1].file_id
    elif message.animation:
        file_id = message.animation.file_id
    elif message.video:
        file_id = message.video.file_id
    elif message.document:
        file_id = message.document.file_id
    return message.reply(file_id)


def private_default(client, message):
    return message.reply(default_reply)


def private_message(client, message):
    user_id = message.from_user.id
    if user_id == developer_id:
        return private_get_file_id(client, message)
    else:
        return private_default(client, message)


def private_unknown(client, message):
    return message.reply(unknown)
