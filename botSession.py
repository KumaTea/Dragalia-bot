import logging
from queue import Queue
from telegram import Bot
from botInfo import self_id
from botTools import query_token
from telegram.ext import Dispatcher
from botSessionWeb import nga, nga_token, driver
from apscheduler.schedulers.background import BackgroundScheduler


dra = Bot(query_token(self_id))
update_queue = Queue()
dp = Dispatcher(dra, update_queue, use_context=True)

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.WARN)

scheduler = BackgroundScheduler(misfire_grace_time=60)
