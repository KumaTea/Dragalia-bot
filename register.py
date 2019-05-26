import botSession
from mdFunctions import *
from mdComic import life, sync_life
from mdMessage import process_msg
from voteProcessor import process_callback
from telegram.ext import MessageHandler, CommandHandler, CallbackQueryHandler, Filters
from botTools import session_update


def register_handlers():
    dp = botSession.dp
    dp.add_handler(CallbackQueryHandler(process_callback))

    dp.add_handler(CommandHandler(['delay', 'ping'], delay))
    dp.add_handler(CommandHandler(['life', 'comic'], life))
    dp.add_handler(CommandHandler('start', private_start, Filters.private))
    dp.add_handler(CommandHandler('help', private_help, Filters.private))
    dp.add_handler(CommandHandler(['en', 'Eng', 'English'], help_en, Filters.private))
    dp.add_handler(CommandHandler(['ja', 'Japanese'], help_ja, Filters.private))

    dp.add_handler(MessageHandler(Filters.group, process_msg))
    dp.add_handler(MessageHandler((Filters.command & Filters.private), private_unknown))
    dp.add_handler(MessageHandler(Filters.private, private_default))

    return True


def manager():
    botSession.scheduler.add_job(session_update, 'cron', [botSession.nga, botSession.nga_token], hour=4)
    botSession.scheduler.add_job(sync_life, 'cron', hour=14, minute=1)
