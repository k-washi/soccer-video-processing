import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils.config
import logging

import glob


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

def file_list(dir_path, ext):
    if not dir_exsist(dir_path):
        logging.error("ディレクトリが存在しません")
        return []
    f_reg = os.path.join(dir_path, "*." + ext)
    f_list = glob.glob(f_reg)

    if len(f_list) == 0:
        logging.info("{0} に{1}の拡張子を持つファイルが存在しません".format(dir_path, ext))

    return f_list

if __name__ == "__main__":
    dir_path = "../../data/soccer"
    flist = file_list(dir_path, "h5")
    #logging.debug(flist)


