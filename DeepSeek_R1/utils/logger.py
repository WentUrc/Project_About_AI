# utils/logger.py
import logging

def init_logger():
    logging.basicConfig(
        filename='kailiu_chat.log',
        level=logging.INFO,
        format='【%(asctime)s】%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
