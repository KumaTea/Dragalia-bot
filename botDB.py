from botInfo import version, channel


start_message = '/help'
help_message = f'这个bot可以：抓取和转发新闻到 @DragaliaNews\n' \
               f'获取轻松龙约 /life\n' \
               f'获取NGA论坛链接详情。\n' \
               f'手动报时 /time\n' \
               f'欢迎加入群组 @dragaliazh\n\n/English /Japanese\n' \
               f'Ver.: {version} ({channel})'
help_en = f'Read Dragalia Life: /life\n' \
          f'Welcome to the player group @dragaliazh (in Chinese)\n\n' \
          f'Ver.: {version} ({channel})'
help_ja = f'「ゆるがりあ」を読む /life\n' \
          f'中国語グループ @dragaliazh へようこそ\n\n' \
          f'Ver.: {version} ({channel})'
unavailable_cmd = '这个功能不可用。为什么不试试 /life 呢'
default_reply = '嗯'
unknown = 'I can\'t understand your message or command. You may try /help.'

groups = {
    -1001157490282: {
        'id': -1001157490282,
        'username': 'dragaliazh',
        'lang': 'chs'
    },
    #-1001342436432: {
    #    'id': -1001342436432,
    #    'username': 'Dragalia_Lost',
    #    'lang': 'cht'
    #}
}

lang_code = {
    'chs': ['cn', 'sg', 'chs'],
    'cht': ['hk', 'mo', 'tw', 'cht']
}

timer_sticker = {
    'chs': {
        0: 'CAACAgUAAxkBAAIKTV73CLspySzSesZxSiEvh2IQ1OJXAAJ8AAOHNJEU3m8YxWqDORAaBA',  # 12
        # 0: 'CAACAgUAAxkBAAIKT173CMIyRtwBB8oqwBkUPnohpNl_AAJ9AAOHNJEUDY_yh-CQUBEaBA',
        1: 'CAACAgUAAxkBAAIKN173CE5yqY_dhIoNr6gXmxqx46-hAAJxAAOHNJEUrLU-kzsIozUaBA',
        2: 'CAACAgUAAxkBAAIKOV73CGuPNhVtjlN7xYHNiUAAAZAWYQACcgADhzSRFHXVO-8hr76bGgQ',
        3: 'CAACAgUAAxkBAAIKO173CHSKT4x9sz9cYz_tB3MTOss8AAJzAAOHNJEUccvhZ7YkhtEaBA',
        4: 'CAACAgUAAxkBAAIKPV73CH2j-qeuQpmTk1hCGh1pvvM4AAJ0AAOHNJEU3J3F74htWXAaBA',
        5: 'CAACAgUAAxkBAAIKP173CIYId0KMWIlXqS-PmjqSuYGfAAJ1AAOHNJEU5RhPj8XmuG8aBA',
        6: 'CAACAgUAAxkBAAIKQV73CJMNI8YGfSRjJK9H130u7m8MAAJ2AAOHNJEUZJhl6iyR4ZUaBA',
        7: 'CAACAgUAAxkBAAIKQ173CJkNJFTk-8v2Pk3UbM2tG4tIAAJ3AAOHNJEUhBNx8ylfrtQaBA',
        8: 'CAACAgUAAxkBAAIKRV73CJ80aPYVLacQFTP6g8JHTuc9AAJ4AAOHNJEUYkxRaumBJ7kaBA',
        9: 'CAACAgUAAxkBAAIKR173CKm75CWkqTv89Hj-_0fwsosdAAJ5AAOHNJEUBAwrRtyLweIaBA',
        10: 'CAACAgUAAxkBAAIKSV73CK5CcW5RT8ARQqU7B2zHqSr7AAJ6AAOHNJEUZ_RROtFhbRMaBA',
        11: 'CAACAgUAAxkBAAIKS173CLOxC_8tTumbPKR8O9ZAXDxRAAJ7AAOHNJEUvZWuBJLoC1kaBA',
        12: 'CAACAgUAAxkBAAIKTV73CLspySzSesZxSiEvh2IQ1OJXAAJ8AAOHNJEU3m8YxWqDORAaBA'
    },
    'cht': {
        0: 'CAACAgUAAxkBAAIKbF7-rJsn1fYZP_LbhDkSqtLtC_-bAAKfAAOHNJEUOQeTDslXCCQaBA',  # 12
        # 0: 'CAACAgUAAxkBAAIKbl7-rKW_wQuj3gMLS6hJAcgbkx6vAAKhAAOHNJEUKJJwXaeS4cYaBA',
        1: 'CAACAgUAAxkBAAIKZl7-rHGZMLsX0yK0Z4Rku90M2qenAAKTAAOHNJEUwZyaw7W3xMQaBA',
        2: 'CAACAgUAAxkBAAIKaF7-rIer8O4SDCn0GArUJuYhSKLjAAKUAAOHNJEU6QABRj31YHbCGgQ',
        3: 'CAACAgUAAxkBAAIKal7-rJAYNgYePubPch_V-jsyrT_MAAKVAAOHNJEU6Mtp7M5zKuIaBA',
        4: 'CAACAgUAAxkBAAIKcF7-rLFGsylLSu9JDHFc_pje02knAAKWAAOHNJEUaYxAex0IySgaBA',
        5: 'CAACAgUAAxkBAAIKcl7-rMQDvzE9d60Dqbq8oXojJ3EPAAKXAAOHNJEUp-hW-D9gCOEaBA',
        6: 'CAACAgUAAxkBAAIKdF7-rNdVS1Z0bMCPz6OgU1NFo4zmAAKYAAOHNJEUejN07MBbB2waBA',
        7: 'CAACAgUAAxkBAAIKdl7-rOCtmE8Y52V23VtyneYTt81eAAKaAAOHNJEUQsvj2N4-xA4aBA',
        8: 'CAACAgUAAxkBAAIKeF7-rOYsom-w8QlJ2PHrmbjy9w8eAAKbAAOHNJEU43_dNHUMBN8aBA',
        9: 'CAACAgUAAxkBAAIKel7-rOzC8QYmNPAP2oJeDj2eYm4dAAKcAAOHNJEUron9MKJLbH0aBA',
        10: 'CAACAgUAAxkBAAIKfF7-rPO4HEZDVoS_T06iuEZ5OysSAAKdAAOHNJEU0Ud-imzdA5waBA',
        11: 'CAACAgUAAxkBAAIKfl7-rP0CHTDkJvxC59xBReer2HiQAAKeAAOHNJEUoNBZEv7FDjIaBA',
        12: 'CAACAgUAAxkBAAIKgF7-rQbnTItxThVpaYnkd8aPzCRYAAKfAAOHNJEUOQeTDslXCCQaBA'
    }
}


url_blacklist = [
    'nuke', 'setting', 'message', 'compose',
    'login', 'logout', 'sign', 'register'
]


loading_image = [
    'AgACAgQAAx0ESGhsZQADsGE_gK-LhRDxIAznPtuIkziC-UUMAAIFrTEb3yr8UVwkqc0je_e-AQADAgADeAADIAQ',  # 108
    'AgACAgQAAx0ESGhsZQADrGE_gETOaVLO-GXatvRv5x50iV6_AAImrTEb9_z9UY_i__qvtXVGAQADAgADeAADIAQ',  # 119
    'AgACAgQAAx0ESGhsZQADrmE_gE6wLWHnlTMHmJTVZKMnUu9SAAJXrDEbenoFUp3m1SAGeOBNAQADAgADeAADIAQ',  # 198
    'AgACAgQAAx0ESGhsZQADpGE_f8PnCtGEQ140iMhHyKx_D90qAAIQrTEb-wf9UQST0Rj69dQHAQADAgADeAADIAQ',  # 242
    'AgACAgQAAx0ESGhsZQADomE_f7VEMfUIPKOX-IW7TZ__ygABJgACA60xG0Jl_VHuysD-UfKd3AEAAwIAA3gAAyAE',  # 267
    'AgACAgQAAx0ESGhsZQADpmE_f8peLwhIjzis8BdOQUVKlYMmAAIFrTEbdjv8UfpmwSP6hHkPAQADAgADeAADIAQ',  # 340
    'AgACAgQAAx0ESGhsZQADqGE_f9S3RAq02zyDENDd94Crv-CoAALSrDEb1j_9UZngiGlZVqKvAQADAgADeAADIAQ',  # 342
    'AgACAgQAAx0ESGhsZQADqmE_f-tVp77emB_00Nc0SMuIqY8UAAL-rDEbuwX8UQYdSHbpqh9CAQADAgADeAADIAQ',  # 381
]
