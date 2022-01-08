import botCache
from time import time
# from botDB import groups
from botSession import dra
from botInfo import self_id


special_ids = [
    100, 1000, 10000, 100000, 1000000
]
for i in special_ids.copy():
    for j in range(1, 10):
        special_ids.append(i*j)
special_ids.extend([114514, 1919, 810, 1919810])


done = ['好了', '可以']
thanks = ['\u8C22', '\u5C04']
extension = {
    'image': {
        'good': '.webp',
        'bad': ['.jpg', '.bmp']
    },
    # audio
    'video': {
        'good': '.mp4',
        'bad': ['.avi', '.rm']
    },
}


def process_id(chat_id, message_id):
    if message_id in special_ids:
        dra.send_message(chat_id, f'祝贺本群第**{message_id}**条消息达成！ 🎉', parse_mode='Markdown')
        if dra.get_chat_member(chat_id, self_id).can_pin_messages:
            dra.pin_chat_message(chat_id, message_id, True)
    return True


def process_keyword(message):
    text = message.text
    if message.caption and not text:
        text = message.caption
    """
    for item in extension:
        for word in extension[item]['bad']:
            if word in text:
                return message.reply_text(
                    '本群推荐弃用野蛮的 ' + word + ' 格式，使用文明的 ' + extension[item]['good'] + ' 格式。',
                    quote=False)
    """
    for word in done:
        if f'我{word}' in text:
            return message.reply_text(f'我也{word}', quote=False)
    for word in thanks:
        if f'已经{word}了' in text or f'我{word}了' in text:
            return message.reply_text(f'我也{word}了', quote=False)
    return None


def last_msg(chat_id):
    botCache.last_msg_time[chat_id] = time()  # int(time())


def process_msg(update, context):
    message = update.message
    try:
        chat_id = message.chat_id
    except AttributeError:
        return None  # edited message
    message_id = message.message_id
    text = message.text

    # process_id(chat_id, message_id)

    # if chat_id in groups:
    #     last_msg(chat_id)

    if message.caption and not text:
        text = message.caption
    if text:
        return process_keyword(message)
    else:
        return None
