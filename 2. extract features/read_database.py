import read_YUV420 as ry420
import numpy as np


def readvideo(targetfrm, video_dir, frame_detail):
    video_name = frame_detail[0]
    framenum = frame_detail[1]
    col = frame_detail[2]
    row = frame_detail[3]

    temp = np.zeros((1, framenum, row, col, 3), dtype=np.uint8)
    temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
        video_dir + '/' + str(video_name) + '.yuv', row, col, framenum, targetfrm)
    return temp, framenum, col, row
