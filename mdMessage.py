from botInfo import self_id
from botSession import dra
from mdNGA import nga_link_process


special_ids = [
    100, 1000, 10000, 100000, 1000000,
    114514, 1919, 810, 1919810, 1145141919,
]


done = ['好了', '可以']
thanks = ['\u8C22', '\u5C04']


def process_id(chat_id, message_id):
    if message_id in special_ids:
        dra.send_message(chat_id, f'祝贺本群第**{message_id}**条消息达成！ 🎉', parse_mode='Markdown')
        if dra.get_chat_member(chat_id, self_id).can_pin_messages:
            dra.pin_chat_message(chat_id, message_id, True)
    return True


def process_keyword(message):
    text = message.text
    for word in done:
        if f'我{word}' in text:
            return message.reply_text(f'我也{word}', quote=False)
    for word in thanks:
        if f'已经{word}了' in text or f'我{word}了' in text:
            return message.reply_text(f'我也{word}了', quote=False)
    return None


def process_msg(update, context):
    message = update.message
    # chat_id = message.chat_id
    # message_id = message.message_id
    text = message.text

    # process_id(chat_id, message_id)

    if message.caption and not text:
        text = message.caption
    if text:
        process_keyword(message)
        return nga_link_process(message)
    else:
        return None
