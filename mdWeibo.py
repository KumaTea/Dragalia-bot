import re
from botSession import dra
from mdScreen import get_screenshot


weibo_url = ['weibo.com', 'www.weibo.com', 'm.weibo.com',
           'weibo.cn', 'www.weibo.cn', 'm.weibo.cn']


def escape_md(text):
    markdown_char = ['*', '_', '`']  # '[', ']',
    for item in markdown_char:
        text = text.replace(item, f'\\{item}')
    return text


def weibo_link_process(message):
    chat_id = message.chat_id
    text = message.text
    if not text:
        return None

    weibo_domain = None
    if 'http' not in text:
        url = ''
        for domain in weibo_url:
            if domain in text:
                weibo_domain = domain
                text = text.replace(domain, f'https://{domain}')
                url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                 text)[0]
        if not weibo_domain:
            return None
    else:
        url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        if url:
            url = url[0]
        else:
            return None
        for domain in weibo_url:
            if domain in url:
                weibo_domain = domain
        if not weibo_domain:
            return None
    url = url.replace('http://', 'https://')

    inform = dra.send_message(chat_id, 'Weibo link found. Retrieving...')
    inform_id = inform.message_id

    dra.send_chat_action(chat_id, 'upload_photo')
    screenshot = get_screenshot(url)
    dra.delete_message(chat_id, inform_id)
    return dra.send_photo(chat_id, screenshot)
