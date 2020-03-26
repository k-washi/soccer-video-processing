import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils.config
import logging
import cv2

from video_processing.io import VideoCapture


def show_video(video_name, output_dir = ""):
    vc = VideoCapture(video_name)

    while True:
        ret = vc.read()
        if ret:
            vc.imshow(window_name="show")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif cv2.waitKey(1) & 0xFF == ord('s') and output_dir != "":
                vc.save(output_dir)
        else:
            break

    del vc

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='path to video')
    parser.add_argument('-o', default="", help='path to dir for img save')

    args = parser.parse_args()

    video_name = args.i
    output_dir = args.o

    show_video(video_name, output_dir)