"""
videoファイルを読み込んで、h5ファイル形式で、保存する。

# example

python ./src/data_formation.py -i ../../data/soccer/test.mp4 -o ../../data/soccer/test.h5 -s 30 -n 100 -f 2

"""
import os
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils.config
import logging
import h5py

from video_processing.io import VideoCapture
from utils.h5_processing import extention_check_h5, H5_HWC, H5_VIDEO
from utils.path_translate import add_ID_to_path


def data_formation(video_name, output_file, img_num=1000, save_num=2, sampling_rate=1):
    vc = VideoCapture(video_name)
    if not extention_check_h5(output_file):
        logging.error("{}の拡張子が間違っている".format(output_file))
        exit(-1)

    data_video = []
    save_count = 1
    while save_count <= save_num:
        ret = vc.read()
        if vc.frame_count % sampling_rate != 0:
            continue

        if ret:
            data_video.append(vc.frame)

            if len(data_video) % img_num == 0:
                # h5ファイルのsave
                f_name = add_ID_to_path(output_file, save_count)

                with h5py.File(f_name, "w") as f:
                    hwc = np.array([vc.HEIGHT, vc.WIDTH, vc.CHANNEL])
                    data_hwc = f.create_dataset(name=H5_HWC, data=hwc)

                    save_video = np.array(data_video)
                    save_video = f.create_dataset(name=H5_VIDEO, data=save_video)
                    logging.info("{}を保存しました。".format(f_name))

                save_count += 1
                data_video = []
        else:
            break

    del vc


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='path to video')
    parser.add_argument('-o', default="", help='path to dir for img save')
    parser.add_argument('-n', default=1000, type=int, help="1ファイルに保存するデータの数")
    parser.add_argument('-f', default=2, type=int, help="保存するファイル数")
    parser.add_argument('-s', default=1, type=int, help="動画のサンプリング間隔")

    args = parser.parse_args()

    video_name = args.i
    output_dir = args.o
    img_num = args.n
    save_num = args.f
    sampling_rate = args.s

    data_formation(video_name, output_dir, img_num=img_num, save_num=save_num, sampling_rate=sampling_rate)
