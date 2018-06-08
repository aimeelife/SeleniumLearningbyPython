#encoding=utf-8
import logging.config

logging.config.fileConfig("Logger.conf")

def debug(message):
    logging.debug(message)

def warnning(message):
    logging.warnning(message)

def info(message):
    logging.info(message)
