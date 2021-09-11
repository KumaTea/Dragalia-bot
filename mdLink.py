from mdNGA import nga_link_process


def link_process(message):
    chat_id = message.chat_id
    text = message.text
    if not text:
        return None
