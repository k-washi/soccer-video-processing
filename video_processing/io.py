# coding:utf-8

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils.config
import logging

import cv2

from utils.os_processing import file_exist


def _open_video(video_name):
    if not file_exist(video_name):
        logging.error("{} がありませんでした。".format(video_name))
        sys.exit(-1)

    cam = cv2.VideoCapture(video_name)
    logging.info("{}を開きました。".format(video_name))
    return cam


class video_capture(object):
    def __init__(self, video_name):
        self.cam = _open_video(video_name)

        ret, frame = self.cam.read()
        if ret:
            self.frame = frame

        else:
            logging.error("{}からデータを読み込めませんでした。".format(video_name))
            exit(-1)

    def read(self):
        ret, self.frame = self.cam.read()
        return ret

    def __del__(self):
        if hasattr(video_capture, 'cam'):
            self.cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    video_name = "../../data/soccer/test.mp4"

    video_cap = video_capture(video_name)

    logging.debug("video capture finish!!")
