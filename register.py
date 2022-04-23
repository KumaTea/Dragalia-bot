import logging
from functions import *
from pyrogram import filters
from process_msg import process_msg
from session import dra, scheduler
from comic import life, sync_life
from pyrogram.handlers import MessageHandler


def register_handlers():
    dra.add_handler(MessageHandler(life, filters.command(['life', 'comic']) & ~filters.edited))
    dra.add_handler(MessageHandler(send_time, filters.command(['time', 'timer', 'when', 'hour']) & ~filters.edited))
    dra.add_handler(MessageHandler(private_start, filters.command(['start']) & filters.private & ~filters.edited))
    dra.add_handler(MessageHandler(private_help, filters.command(['help']) & filters.private & ~filters.edited))
    dra.add_handler(MessageHandler(help_english, filters.command(['en', 'Eng', 'English']) & filters.private & ~filters.edited))
    dra.add_handler(MessageHandler(help_japanese, filters.command(['ja', 'Japanese']) & filters.private & ~filters.edited))

    dra.add_handler(MessageHandler(process_msg, filters.group & ~filters.edited))
    dra.add_handler(MessageHandler(private_message, filters.private & ~filters.edited))

    return logging.info('Registered handlers')


def manager():
    scheduler.add_job(sync_life, 'cron', hour=14, minute=1)
    return logging.info('Added job')
