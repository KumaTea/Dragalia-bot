import botSession
from mdFunctions import *
from mdTimer import timer as cron_timer
from mdMessage import process_msg
from mdComic import life, sync_life
from botTools import session_update
from voteProcessor import process_callback
from telegram.ext import MessageHandler, CommandHandler, CallbackQueryHandler, Filters


def register_handlers():
    dp = botSession.dp
    dp.add_handler(CallbackQueryHandler(process_callback))

    dp.add_handler(CommandHandler(['delay', 'ping'], delay))
    dp.add_handler(CommandHandler(['life', 'comic'], life))
    dp.add_handler(CommandHandler(['time', 'timer', 'when', 'hour'], send_time))
    dp.add_handler(CommandHandler('start', private_start, Filters.private))
    dp.add_handler(CommandHandler('help', private_help, Filters.private))
    dp.add_handler(CommandHandler(['en', 'Eng', 'English'], help_english, Filters.private))
    dp.add_handler(CommandHandler(['ja', 'Japanese'], help_japanese, Filters.private))

    dp.add_handler(MessageHandler(Filters.group, process_msg))
    dp.add_handler(MessageHandler((Filters.command & Filters.private), private_unknown))
    dp.add_handler(MessageHandler(Filters.private, private_message))

    return True


def manager():
    scheduler = botSession.scheduler
    scheduler.add_job(session_update, 'cron', [botSession.nga, botSession.nga_token], hour=4)
    scheduler.add_job(sync_life, 'cron', hour=14, minute=1)
    scheduler.add_job(cron_timer, 'cron', hour='*')
