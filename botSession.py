import json
import logging
from requests import Session
from telegram import Bot
from telegram.ext import Dispatcher
from botInfo import self_id
from botTools import query_token
from queue import Queue
from apscheduler.schedulers.background import BackgroundScheduler


dra = Bot(query_token(self_id))
update_queue = Queue()
dp = Dispatcher(dra, update_queue, use_context=True)


nga = Session()
nga_token = json.loads(query_token('nga'))
headers = nga_token['headers']
cookies = nga_token['cookies']
nga.headers.update(headers)
nga.cookies.update(cookies)

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.WARN)

scheduler = BackgroundScheduler(misfire_grace_time=60)
