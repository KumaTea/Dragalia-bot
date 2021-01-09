import re
import time
from urllib import parse
from botSession import dra, nga
from datetime import datetime, timezone, timedelta


nga_url = ['nga.178.com', 'bbs.nga.cn', 'ngabbs.com']


def escape_md(text):
    markdown_char = ['*', '_', '`']  # '[', ']',
    for item in markdown_char:
        text = text.replace(item, f'\\{item}')
    return text


def nga_link_process(message):
    chat_id = message.chat_id
    text = message.text
    if not text:
        return None

    nga_domain = None
    if 'http' not in text:
        url = ''
        for domain in nga_url:
            if domain in text:
                nga_domain = domain
                text = text.replace(domain, f'https://{domain}')
                url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                 text)[0]
        if not nga_domain:
            return None
    else:
        url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        if url:
            url = url[0]
        else:
            return None
        for domain in nga_url:
            if domain in url:
                nga_domain = domain
        if not nga_domain:
            return None
    url = url.replace('http://', 'https://')
    if '&' in url:
        params = parse.parse_qs(parse.urlparse(url).query)
        if 'pid' in params:
            post_id = params['pid'][0]
            url = f'https://bbs.nga.cn/read.php?pid={post_id}'
        elif 'tid' in params:
            thread_id = params['tid'][0]
            url = f'https://bbs.nga.cn/read.php?tid={thread_id}'
        else:
            return False
    url += '&__output=11'

    inform = dra.send_message(chat_id, 'NGA link found. Retrieving...')
    inform_id = inform.message_id

    result = nga.get(url)
    if result.status_code != 200:
        return dra.edit_message_text(f'错误：服务器返回{result.status_code}', chat_id, inform_id)
    else:
        if 'error' in result.json():
            return dra.edit_message_text('错误' + result.json()['error'][0], chat_id, inform_id)
        result_data = result.json()['data']
        title = escape_md(result_data['__T']['subject'])
        author = result_data['__T']['author']
        author_id = result_data['__T']['authorid']
        date = datetime.fromtimestamp(
            result_data['__T']['postdate'], tz=timezone(timedelta(hours=8))).strftime('%m-%d %H:%M')
        forum = result_data['__F']['name']
        forum_id = result_data['__T']['fid']

        link_result = f'*{title}*\n' \
                      f'[{author}](https://{nga_domain}/nuke.php?func=ucp&uid={author_id}) ' \
                      f'{date} ' \
                      f'[{forum}](https://{nga_domain}/thread.php?fid={forum_id})'
        if title in text:
            dra.edit_message_text('哦，已经有标题了啊，那没事了……', chat_id, inform_id)
            time.sleep(5)
            return dra.delete_message(chat_id, inform_id)
        else:
            return dra.edit_message_text(
                link_result, chat_id, inform_id, parse_mode='Markdown', disable_web_page_preview=True)
