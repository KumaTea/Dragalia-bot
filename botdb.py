import botinfo

# Localization
langlist = ['en', 'ja', 'Hans', 'Hant', 'CN', 'HK', 'TW', 'SG', 'MO']  # no 'zh'
langdict = {
    'zh': 'Hans',  # not 'hans'
    'en': 'en',
    'ja': 'ja',
    'Hans': 'Hans',
    'Hant': 'Hant',
    'CN': 'Hans',
    'HK': 'Hant',
    'TW': 'Hant',
    'SG': 'Hans',
    'MO': 'Hant',
}
hellomsg = {
    'Hans': '你好！你可以通过发送 /help 来获取帮助哦。',
    'Hant': '你好！你可以通過發送 /help 來獲取幫助。',
    'en': 'Hello there!\nYou may see commands sending \"/help\".',
    'ja': 'こんにちは！ /help を送ってヘルプを受け取る下さい。',
}
helpmsg = {
    'Hans': '/start: 唤醒我\n/help: 显示此帮助\n' +
            '/calendar: 龙约历\n/info: 什么是“失落的龙约”?' +
            '\n\n版本{}\n如果您有任何疑问或建议，欢迎提交到 {}'.format(botinfo.version, botinfo.repo),

    'Hant': '/start: 喚醒我\n/help: 顯示此幫助\n' +
            '/calendar: 龍絆日曆\n/info: 什麼是“失落的龍絆”?' +
            '\n\n版本{}\n如果您有任何疑問或建議，歡迎提交到 {}'.format(botinfo.version, botinfo.repo),

    'en': '/start: wake me up\n/help: display this message\n' +
          '/calendar: display Dragalian Calendar\n/info: what\'s Dragalia Lost?' +
          '\n\nVersion {}\nIf you have any issue or suggestion, please submit at {}'.format(botinfo.version, botinfo.repo),

    'ja': '/start: 私が来た！\n/help: 此のヘルプを表示\n' +
          '/calendar: ドラガリ暦\n/info: ドラがリアロストとは' +
          '\n\n版本{}\n何か問題や提案がある場合は、 {} で送信して下さい'.format(botinfo.version, botinfo.repo),
}

priverror = {
    'Hans': '搜索功能正在开发中，请等待。',
    'Hant': '搜索功能正在開發中，請等待。',
    'en': 'Plain text searching is still under development. Please wait for future updates.',
    'ja': '検索機能はまだ開発中です。 今後のアップデートをお待ち下さい。'
}

grperror = {
    'Hans': '搜索功能正在开发中，请等待。',
    'Hant': '搜索功能正在開發中，請等待。',
    'en': 'Plain text searching is still under development. Please wait for future updates.',
    'ja': '検索機能はまだ開発中です。 今後のアップデートをお待ち下さい。'
}

cmderror = {
    'Hans': '我无法理解这条命令！您可以查看 /help 帮助列表。',
    'Hant': '我無法理解這條命令！您可以查看 /help 幫助列表。',
    'en': 'I can\'t understand your command. You may check the /help list.',
    'ja': '理解出来ません！ /help を見る下さい。'
}
# Not enabled
grpwelcome = {
    -1234567890: {
        'name': 'Example group',
        'message': 'Example welcome message',
        'sticker': 'ExAmPlEwElCoMeStIcKeR',
    },
}
