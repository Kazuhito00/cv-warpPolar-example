#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[summary]
  極座標変換サンプル(動画版)
[description]
  -
"""

import argparse
import copy

import cv2 as cv


def get_args():
    """
    [summary]
        引数解析
    Parameters
    ----------
    None
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--width", help='capture width', type=int, default=960)
    parser.add_argument(
        "--height", help='capture height', type=int, default=540)

    args = parser.parse_args()

    return args


def main():
    """
    [summary]
        main()
    Parameters
    ----------
    None
    """
    # 引数解析 #################################################################
    args = get_args()
    cap_width = args.width
    cap_height = args.height

    # カメラ準備 ###############################################################
    cap = cv.VideoCapture('image/clock.mp4')
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    while True:
        # カメラキャプチャ #####################################################
        ret, frame = cap.read()
        if not ret:
            print('cap.read() error')
            break

        # 極座標変換
        rotate_frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
        lin_polar_image = cv.warpPolar(
            rotate_frame, (150, 500), (270, 480), 220,
            cv.INTER_CUBIC + cv.WARP_FILL_OUTLIERS + cv.WARP_POLAR_LINEAR)

        # トリミング/向き調整
        lin_polar_crop_image = copy.deepcopy(lin_polar_image[0:500, 15:135])
        lin_polar_crop_image = lin_polar_crop_image.transpose(1, 0, 2)[::-1]

        # 描画
        cv.imshow('ORIGINAL', frame)
        cv.imshow('POLAR', lin_polar_crop_image)

        # キー入力(ESC:プログラム終了) #########################################
        key = cv.waitKey(50)
        if key == 27:  # ESC
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
