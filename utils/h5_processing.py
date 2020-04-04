import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils.config
import logging

import h5py

H5_HWC = 'img/hwc'
H5_VIDEO = 'video/data'


def extention_check_h5(file_name):
    _, ext = os.path.splitext(file_name)
    if ext == ".h5" or ext == ".hdf5":
        return True
    return False


def read_h5(file_name):
    if not extention_check_h5(file_name):
        logging.error("ファイル名が間違っている: {}".format(file_name))

    with h5py.File(file_name, 'r') as f:
        hwc = f[H5_HWC][:]
        data = f[H5_VIDEO][:]


        logging.info("{} を読み込みました".format(file_name))
        return hwc, data

    return None, None


if __name__ == "__main__":
    path = "../../data/soccer/test_1.h5"
    hwc, data = read_h5(path)
    print(hwc)
    print(data.shape)