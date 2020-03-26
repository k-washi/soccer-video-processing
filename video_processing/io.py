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


class VideoCapture(object):
    def __init__(self, video_name):
        self.cap = _open_video(video_name)
        self.frame_count = 0

        ret, frame = self.cap.read()

        if ret and self.cap.isOpened():
            self.frame = frame
            self.HEIGHT, self.WIDTH, self.CHANNEL = self.frame.shape  # (高さ, 幅, チャンネル)の順

        else:
            logging.error("{}からデータを読み込めませんでした。".format(video_name))
            exit(-1)


    def read(self):
        ret, frame = self.cap.read()
        if ret:
            self.frame = frame.copy()
            self.frame_count += 1
        return ret

    def imshow(self, window_name):
        cv2.imshow(window_name, self.frame)

    def save(self, output_dir):
        output_path = os.path.join(output_dir, str(self.frame_count) + '.jpg')
        cv2.imwrite(output_path, self.frame)
        logging.info("{}が保存されました".format(output_path))

    def __del__(self):
        if hasattr(VideoCapture, 'cam'):
            self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    video_name = "../../data/soccer/test.mp4"

    video_cap = VideoCapture(video_name)

    logging.debug("video capture finish!!")
