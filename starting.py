import logging
from tools import mkdir
from session import scheduler
from register import register_handlers, manager


def starting():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    mkdir(['tmp', 'life', '../vote'])
    register_handlers()
    manager()
    scheduler.start()
    return logging.info("Initialized.")
