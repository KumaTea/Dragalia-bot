from botDB import *
from botSession import dra
from datetime import datetime
from botInfo import developer_id
from botTools import detect_lang


def delay(update, context):
    chat_id = update.message.chat_id
    first_timestamp = int(datetime.timestamp(update.message.date))

    checking_message = update.message.reply_text('Checking delay...')

    second_timestamp = int(datetime.timestamp(checking_message.date))
    second_msg_id = checking_message.message_id
    duration = second_timestamp - first_timestamp
    if duration == 0:
        status = 'excellent'
    elif duration == 1:
        status = 'good'
    else:
        status = 'bad'
    return dra.edit_message_text(f'Delay is {duration}s.\nThe connectivity is {status}.', chat_id, second_msg_id)


def send_time(update, context):
    message = update.message
    chat_id = message.chat_id

    now = datetime.now()
    lang = detect_lang(message)
    hour = int(now.strftime('%I'))
    sticker = timer_sticker[lang][hour]
    return dra.send_sticker(chat_id, sticker)


def private_start(update, context):
    return update.message.reply_text(start_message)


def private_help(update, context):
    return update.message.reply_text(help_message)


def help_english(update, context):
    return update.message.reply_text(help_en)


def help_japanese(update, context):
    return update.message.reply_text(help_ja)


def private_get_file_id(update, context):
    file_id = 'Unknown type of media.'
    if update.message.text:
        file_id = update.message.text
    elif update.message.sticker:
        file_id = update.message.sticker.file_id
    elif update.message.photo:
        file_id = update.message.photo[-1].file_id
    elif update.message.animation:
        file_id = update.message.animation.file_id
    elif update.message.video:
        file_id = update.message.video.file_id
    elif update.message.document:
        file_id = update.message.document.file_id
    return update.message.reply_text(file_id)


def private_default(update, context):
    return update.message.reply_text(default_reply)


def private_message(update, context):
    user_id = update.message.from_user.id
    if user_id == developer_id:
        return private_get_file_id(update, context)
    else:
        return private_default(update, context)


def private_unknown(update, context):
    return update.message.reply_text(unknown)
