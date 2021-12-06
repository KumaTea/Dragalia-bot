import re
import time
import subprocess
from botDB import *
from urllib import parse
from random import choice
from telegram import InputMediaPhoto
from botTools import mention_other_bot
from botSession import dra, nga, driver
from datetime import datetime, timezone, timedelta
from mdScreen import get_screenshot, reset_browser


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
        for domain in nga_domains:
            if domain in text:
                nga_domain = domain
                text = text.replace(domain, f'https://{domain}')
                url = re.findall(url_regex, text)[0]
        if not nga_domain:
            return None
    else:
        url = re.findall(url_regex, text)
        if url:
            url = url[0]
        else:
            return None
    url_domain = parse.urlparse(url).netloc
    if url_domain.lower() not in nga_domains:
        return None
    for keyword in url_blacklist:
        if keyword in url:
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
    url_for_screenshot = url
    url += '&__output=11'
    if mention_other_bot(text, url_for_screenshot):
        return None

    # inform = dra.send_message(chat_id, 'NGA link found. Retrieving...')
    inform = dra.send_photo(chat_id, choice(loading_image), caption='NGA link found. Retrieving...')
    inform_id = inform.message_id

    result = nga.get(url)
    if result.status_code != 200:
        # return dra.edit_message_text(f'错误：服务器返回{result.status_code}', chat_id, inform_id)
        return dra.edit_message_caption(chat_id, inform_id, caption=f'错误：服务器返回{result.status_code}')
    else:
        if 'error' in result.json():
            # return dra.edit_message_text('错误' + result.json()['error'][0], chat_id, inform_id)
            return dra.edit_message_caption(chat_id, inform_id, caption=('错误' + result.json()['error'][0]))
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
            # dra.edit_message_text('哦，已经有标题了啊，那没事了……', chat_id, inform_id)
            dra.edit_message_caption(chat_id, inform_id, caption='哦，已经有标题了啊，那没事了……')
            time.sleep(5)
            return dra.delete_message(chat_id, inform_id)
        else:
            dra.send_chat_action(chat_id, 'upload_photo')
            screenshot = get_screenshot(url_for_screenshot)
            # dra.delete_message(chat_id, inform_id)
            # return dra.send_photo(chat_id, screenshot, caption=link_result, parse_mode='Markdown')
            dra.edit_message_media(chat_id, inform_id, media=InputMediaPhoto(screenshot))
            dra.edit_message_caption(chat_id, inform_id, caption=link_result, parse_mode='Markdown')
            reset_browser()
            return True


def check_nga_login():
    login_success_text = 'KumaTea'
    driver.get(f'https://{nga_domains[1]}/')  # 'bbs.nga.cn'
    if login_success_text in driver.page_source:
        result = True
    else:
        result = False
        subprocess.run([notify_path, '[DRA] NGA login failed'])
    reset_browser()
    return result
