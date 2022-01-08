import os
import json
from botSession import dra
from voteGenerator import gen_reply_markup


def process_callback(update, context):
    """
    Steps:
    1. Edit vote data
    2. Inform user
    3. Change button text
    """
    callback_query = update.callback_query
    callback_message = callback_query.message

    chat_id = callback_message.chat.id
    msg_id = callback_message.message_id

    user_id = callback_query.from_user.id
    callback_id = callback_query.id
    vote_id = json.loads(callback_query.data)['id']
    choice = json.loads(callback_query.data)['e']
    choice_result = ''

    # STEP 1: Processing data

    if os.path.isfile('../../vote/vote.json'):
        with open('../../vote/vote.json', 'r') as file:
            vote_data = json.load(file)
            if vote_id in vote_data:
                vote_json = vote_data[vote_id]
            else:
                vote_json = recover_vote(callback_query)

    else:
        vote_data = {}
        vote_json = recover_vote(callback_query)

    for item in vote_json['options']:
        if user_id in vote_json['options'][item]:
            vote_json, choice_result = process_vote_choice(vote_json, user_id, choice, item)
            break
    if not choice_result:
        vote_json, choice_result = process_vote_choice(vote_json, user_id, choice)

    vote_data[vote_id] = vote_json
    with open('../../vote/vote.json', 'w') as file:
        json.dump(vote_data, file)

    # STEP 1 END

    # STEP 2: Edit button text

    dra.edit_message_reply_markup(chat_id, msg_id, reply_markup=gen_reply_markup(vote_id, vote_json=vote_json))

    # STEP 2 END

    # STEP 3: Infrom user

    if 'new' in choice_result:
        inform = f'You chose {choice}.'
    elif 'change' in choice_result:
        inform = f'You changed to {choice}.'
    else:
        inform = f'You cancelled your choice.'

    dra.answer_callback_query(callback_id, inform)

    # STEP 3 END

    return 'Vote successful processed.'


def recover_vote(callback_query):
    reply_markup = callback_query.message.reply_markup
    vote_id = json.loads(callback_query.data)['id']
    vote_json = {
        'info': {
            'id': vote_id,
            'time': vote_id[4:],
            'options': [],
            'participants': 0,
        },
        'options': {},
    }

    for item in reply_markup.inline_keyboard[0]:
        option_text = item.text
        option = json.loads(item.callback_data)['e']
        vote_json['options'][option] = []
        vote_json['info']['options'].append(option)
        if option_text != option:
            if [int(s) for s in option_text.split() if s.isdigit()] is not []:
                member_count = [int(s) for s in option_text.split() if s.isdigit()][-1]
                vote_json['info']['participants'] += member_count
                for i in range(member_count):
                    vote_json['options'][option].append(i+1)

    with open('../../vote/vote.json', 'r') as file:
        vote_data = json.load(file)
    vote_data[vote_id] = vote_json
    with open('../../vote/vote.json', 'w') as file:
        json.dump(vote_data, file)

    return vote_json


def process_vote_choice(vote_json, user, choice, original=None):
    if original:
        if choice == original:
            vote_json['info']['participants'] -= 1
            vote_json['options'][choice].remove(user)
            return vote_json, 'cancelled'
        else:
            vote_json['options'][choice].append(user)
            vote_json['options'][original].remove(user)
            return vote_json, 'changed'
    else:
        vote_json['info']['participants'] += 1
        vote_json['options'][choice].append(user)
        return vote_json, 'newly added'
