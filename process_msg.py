from session import dra
from info import self_id


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
            dra.pin_chat_message(chat_id, message_id, disable_notification=True)
    return True


def process_keyword(message):
    text = message.text
    if message.caption and not text:
        text = message.caption
    for word in done:
        if f'我{word}' in text:
            return message.reply(f'我也{word}')
    for word in thanks:
        if f'已经{word}了' in text or f'我{word}了' in text:
            return message.reply(f'我也{word}了')
    return None


def process_msg(client, message):
    text = message.text
    chat_id = message.chat.id
    message_id = message.message_id
    process_id(chat_id, message_id)

    if message.caption and not text:
        text = message.caption
    if text:
        return process_keyword(message)
    else:
        return None
