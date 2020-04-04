import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import configparser
import logging
import logging.handlers

from utils.os_processing import file_exist

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), '../setting.ini')
LOG_FORMAT = '%(asctime)s | %(filename)-12s - %(funcName)-12s : %(lineno)-4s | %(levelname)-8s | %(message)s'

if not file_exist(CONFIG_FILE_PATH):
    logging.error("setting.ini ファイルが存在しません。")
    exit(-1)

__config_ini = configparser.ConfigParser()
__config_ini.read(CONFIG_FILE_PATH, encoding='utf-8')


# ログファイルの設定
try:
    __SYSTEM = __config_ini['SYSTEM']
    LOG_LEVEL = __SYSTEM['LOG_LEVEL']

    if LOG_LEVEL == "DEBUG":
        logging.getLogger().setLevel(logging.DEBUG)
    elif LOG_LEVEL == "INFO":
        logging.getLogger().setLevel(logging.INFO)
    elif LOG_LEVEL == "ERROR":
        logging.getLogger().setLevel(logging.ERROR)
    else:
        logging.error("LOG_LEVELの設定が間違っています")

    __LOG_FILE = __SYSTEM['LOG_FILE']
    __LOGGER_FORMAT = logging.Formatter(LOG_FORMAT)

    if str.isdigit(__LOG_FILE):
        if int(__LOG_FILE) == 1:
            log_file = os.path.join(os.path.dirname(__file__), '../log/olog.log')
            fh = logging.handlers.RotatingFileHandler(log_file, maxBytes=100000, backupCount=10)
            # fh = logging.FileHandler(log_file)
            fh.setFormatter(__LOGGER_FORMAT)
            logging.getLogger().addHandler(fh)

    sh = logging.StreamHandler()
    sh.setFormatter(__LOGGER_FORMAT)
    logging.getLogger().addHandler(sh)
except Exception as e:
    logging.error("SYSTEM パラメータの設定が間違っている {}".format(e))

logging.debug("設定が終了しました。")
