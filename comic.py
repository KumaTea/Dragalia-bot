import json
import pickle
import logging
import requests
from PIL import Image
from session import dra
from tools import detect_lang
from info import player_group
from pyrogram.types import InputMediaPhoto


METHOD = 'POST'
languages = ['chs', 'cht', 'en', 'jp']
life_name = {
    'chs': '轻松龙约',
    'cht': '輕鬆龍絆',
    'en': 'Dragalia Life',
    'jp': 'ゆるがりあ',
}
life_box = {
    'cover': (0, 0, 608, 666),
    'content': [
        (0, 700, 608, 1160),
        (0, 1200, 608, 1660),
        (0, 1700, 608, 2160),
        (0, 2200, 608, 2660),
    ]
}
life_help = '格式: /life\n/life <期数>\n/life <语言>\n/life <期数> <语言>\n\n' \
            '命令别名： /comic\n' \
            '期数（可选）需为纯数字\n' \
            '语言（可选）: `chs` `cht` `en` `jp` `cover`\n' \
            '使用空格分隔参数'

index_url = 'https://comic.dragalialost.com/api/index'
detail_url = 'https://comic.dragalialost.com/api/detail/'  # + id
pager_url = 'https://comic.dragalialost.com/api/pager/0/0/'  # + pager
list_url = 'https://comic.dragalialost.com/api/thumbnail_list/'  # + pager


def get_episode_index(lang='chs', index='last'):
    data = {'lang': lang, 'type': 'dragalialife'}
    dra_life = requests.post(index_url, data=data).json()
    if 'first' in index:
        return int(dra_life['first_episode'])  # int
    else:
        return int(dra_life['latest_comic']['id'])


def create_life():
    life_db = {
        'first': 1,
        'latest': 0,
        'comic': {}
        }

    # GET FIRST EPISODE
    first_episode_id = {}
    for lang in languages:
        first_episode_id[lang] = get_episode_index(lang, 'first')
    """
    first_episode_id = {'chs': 17, 'cht': 25, 'en': 9, 'jp': 1}
    """

    # GET COVER / INIT
    data_chs = {'lang': 'chs', 'type': 'dragalialife'}
    first_pager = requests.post(f'{pager_url}0', data=data_chs).json()
    page_total = requests.post(pager_url + str(first_pager['latest']), data=data_chs).json()['pager'][-1]['pageId']

    for page in range(page_total + 1):
        comic_list = requests.post(list_url + str(page), data=data_chs).json()
        if page == 0:
            life_db['latest'] = int(comic_list[0]['episode_num'])
        for item in comic_list:
            life_db['comic'][int(item['episode_num'])] = {
                'episode_num': int(item['episode_num']),
                'thumbnail_l': item['thumbnail_l'],
                'thumbnail_s': item['thumbnail_s'],
                'chs': {
                    'id': int(item['id']),
                    'original': item['main'],
                    'title': item['title'],
                    'cover': '',
                    'content': []
                }
            }

    # GET IMAGE IN EACH LANGUAGE
    for lang in languages:
        data_lang = {'lang': lang, 'type': 'dragalialife'}
        if lang != 'chs':
            comic_id = first_episode_id[lang]
            while True:
                comic_detail = requests.post(detail_url + str(comic_id), data=data_lang).json()[0]

                life_db['comic'][int(comic_detail['episode_num'])][lang] = {
                    'id': int(comic_detail['id']),
                    'original': comic_detail['cartoon'],
                    'title': comic_detail['title'],
                    'cover': '',
                    'content': []
                }
                # time.sleep(1)

                comic_id = int(comic_detail['prev_cartoon']['id'])
                if comic_id == int(comic_detail['id']):
                    break
    logging.info('Created new life_db')
    return life_db


def sync_life(alert=True):
    need_sync = True
    db_changed = False
    try:
        with open('life/life.p', 'rb') as file:
            life_db = pickle.load(file)
    except FileNotFoundError:
        need_sync = False
        db_changed = True
        life_db = create_life()

    latest_episode = 0
    if need_sync:
        data_chs = {'lang': 'chs', 'type': 'dragalialife'}
        latest_life = requests.post(index_url, data=data_chs).json()
        latest_episode = int(latest_life['latest_comic']['episode_num'])
        current_episode = life_db['latest']

        if current_episode < latest_episode:
            db_changed = True
            # chs
            for i in range(latest_episode - current_episode):
                this_comic = latest_life['items'][i]
                life_db['comic'][int(this_comic['episode_num'])] = {
                    'episode_num': int(this_comic['episode_num']),
                    'thumbnail_l': this_comic['thumbnail_l'],
                    'thumbnail_s': this_comic['thumbnail_s'],
                    'chs': {
                        'id': int(this_comic['id']),
                        'original': this_comic['main'],
                        'title': this_comic['title'],
                        'cover': '',
                        'content': []
                    }
                }

            # not chs
            for lang in languages:
                data_lang = {'lang': lang, 'type': 'dragalialife'}
                if lang != 'chs':
                    latest_life = requests.post(index_url, data=data_lang).json()
                    for i in range(latest_episode - current_episode):
                        this_comic = latest_life['items'][i]
                        life_db['comic'][int(this_comic['episode_num'])][lang] = {
                                'id': int(this_comic['id']),
                                'original': this_comic['main'],
                                'title': this_comic['title'],
                                'cover': '',
                                'content': []
                            }

            life_db['latest'] = latest_episode

    if db_changed:
        life_db['comic'] = dict(sorted(life_db['comic'].items()))
        with open('life/life.p', 'wb') as file:
            pickle.dump(life_db, file, protocol=5)
        with open('life/life.json', 'w') as file:
            json.dump(life_db, file)
        if need_sync and alert:
            dra.send_message(player_group, f'轻松龙约第{latest_episode}期更新啦！快点击 /life 阅读吧')

    return life_db


def send_life(chat_id, episode=None, lang='chs'):
    try:
        with open('life/life.p', 'rb') as file:
            life_db = pickle.load(file)
    except FileNotFoundError:
        dra.send_chat_action(chat_id, 'upload_photo')
        life_db = sync_life()

    if not episode:
        episode = life_db['latest']
    elif episode < 1:
        return dra.send_message(chat_id, f'期数{episode}不合法，请重试。')
    elif episode > life_db['latest']:
        return dra.send_message(chat_id, f'第{episode}期暂未更新，请等待更新或使用 `/life refresh` 强制刷新。',
                                parse_mode='Markdown')

    if lang == 'cover':
        if 'http' in life_db['comic'][episode]['thumbnail_l']:
            cover = dra.send_photo(
                chat_id, life_db['comic'][episode]['thumbnail_l'], caption=(
                        life_name['chs'] + f' {episode} ' + life_db['comic'][episode]['chs']['title']))
            cover_id = cover.photo.file_id
            life_db['comic'][episode]['thumbnail_l'] = cover_id
            # db_changed = True
        else:
            return dra.send_photo(
                chat_id, life_db['comic'][episode]['thumbnail_l'], caption=(
                        life_name['chs'] + f' {episode} ' + life_db['comic'][episode]['chs']['title']))
    else:
        if life_db['comic'][episode][lang]['cover'] and life_db['comic'][episode][lang]['content']:
            dra.send_photo(
                chat_id, life_db['comic'][episode][lang]['cover'], caption=(
                        life_name[lang] + f' {episode} ' + life_db['comic'][episode][lang]['title']))
            content_group = []
            for image in life_db['comic'][episode][lang]['content']:
                content_group.append(InputMediaPhoto(image))
            return dra.send_media_group(chat_id, content_group)
        else:
            dra.send_chat_action(chat_id, 'upload_photo')
            cover, content = process_image(life_db['comic'][episode][lang]['original'])
            cover_id = dra.send_photo(chat_id, cover, caption=(
                    life_name[lang] + f' {episode} ' + life_db['comic'][episode][lang]['title'])).photo.file_id
            content_group = []
            for i in content:
                content_group.append(InputMediaPhoto(i))
            content_group_id = dra.send_media_group(chat_id, content_group)
            content_id = []
            for msg in content_group_id:
                content_id.append(msg.photo.file_id)
            life_db['comic'][episode][lang]['cover'] = cover_id
            life_db['comic'][episode][lang]['content'] = content_id
            # db_changed = True

    # if db_changed:
    with open('life/life.p', 'wb') as file:
        pickle.dump(life_db, file, protocol=5)
    return True


def process_image(original):
    with open(f'tmp/original.png', 'wb') as image:
        image.write(requests.get(original).content)
    with Image.open('tmp/original.png') as image:
        cover = 'tmp/cover.png'
        image.crop(life_box['cover']).save(cover, quality=100)

        content = []
        for i in range(4):
            image.crop(life_box['content'][i]).save(f'tmp/content_{i}.png', quality=100)
            content.append(f'tmp/content_{i}.png')
    return cover, content


def life(client, message):
    chat_id = message.chat.id
    text = message.text

    command = text.split(' ')
    if len(command) == 1:
        lang = detect_lang(message)
        return send_life(chat_id, lang=lang)
    elif len(command) == 2:
        if command[1].isnumeric():
            return send_life(chat_id, int(command[1]))
        else:
            if 'help' in command[1]:
                return message.reply(life_help, parse_mode='Markdown')
            elif 'cover' in command[1]:
                return send_life(chat_id, lang='cover')
            elif 're' in command[1]:
                with open('life/life.p', 'rb') as file:
                    old_db = pickle.load(file)
                old = old_db['latest']
                new = sync_life(False)['latest']
                if new > old:
                    return message.reply(f'刷新成功，最新期数为 /life {new}')
                else:
                    return message.reply(f'刷新失败，最新期数为{old}。')
            else:
                for lang in languages:
                    if lang in command[1]:
                        return send_life(chat_id, lang=lang)
                return message.reply('参数错误。请查看 `/life help`', parse_mode='Markdown')
    else:
        if command[1].isnumeric():
            if 'cover' in command[2]:
                return send_life(chat_id, int(command[1]), 'cover')
            else:
                for lang in languages:
                    if lang in command[2]:
                        return send_life(chat_id, int(command[1]), lang)
        return message.reply('参数错误。请查看 `/life help`', parse_mode='Markdown')
