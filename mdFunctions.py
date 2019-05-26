from botDB import *
from datetime import datetime
from botSession import dra


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
    result = dra.edit_message_text(f'Delay is {duration}s.\nThe connectivity is {status}.', chat_id, second_msg_id)
    return result


def private_start(update, context):
    return update.message.reply_text(start_message)


def private_help(update, context):
    return update.message.reply_text(help_message)


def help_en(update, context):
    return update.message.reply_text(help_en)


def help_ja(update, context):
    return update.message.reply_text(help_ja)


def private_default(update, context):
    return update.message.reply_text(default_reply)


def private_unknown(update, context):
    return update.message.reply_text(unknown)
