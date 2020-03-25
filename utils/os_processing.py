import os

import utils.config
import logging

logger = logging.getLogger(__name__)


def dir_exsist(dir_path):
    return os.path.isdir(dir_path)


def dir_create(dir_path):
    try:
        os.makedev(dir_path)
        logging.info("{}を作成しました".format(dir_path))
    except OSError:
        logging.error('Creating directory of data: {}'.format(dir_path))
        exit(-1)

def file_exist(file_path):
    return os.path.isfile(file_path)

