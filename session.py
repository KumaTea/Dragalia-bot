from pyrogram import Client
from apscheduler.schedulers.background import BackgroundScheduler


dra = Client('dra')
scheduler = BackgroundScheduler(misfire_grace_time=60, timezone='Asia/Shanghai')
