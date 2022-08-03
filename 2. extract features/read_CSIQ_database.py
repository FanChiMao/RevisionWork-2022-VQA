import read_YUV420 as ry420
import numpy as np


def readvideo(targetfrm, video_type, count):
    row = 480
    col = 832
    if video_type == 0 or video_type == 1:
        framenum = 600
    elif video_type == 2 or video_type == 3 or video_type == 10:
        framenum = 500
    elif video_type == 4:
        framenum = 250
    elif video_type == 5 or video_type == 8 or video_type == 9:
        framenum = 240
    elif video_type == 6 or video_type == 7 or video_type == 11:
        framenum = 300
    temp = np.zeros((1, framenum, row, col, 3), dtype=np.uint8)
    if video_type == 0:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BQMall_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BQMall_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BQMall_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 1:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BQTerrace_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BQTerrace_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BQTerrace_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 2:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BasketballDrive_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BasketballDrive_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/BasketballDrive_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 3:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Cactus_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Cactus_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Cactus_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 4:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Carving_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Carving_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Carving_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 5:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Chipmunks_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Chipmunks_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Chipmunks_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 6:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Flowervase_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Flowervase_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Flowervase_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 7:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Keiba_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Keiba_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Keiba_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 8:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Kimono_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Kimono_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Kimono_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 9:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/ParkScene_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/ParkScene_832x480_dst_0{}.yuv'.format(count), row, col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/ParkScene_832x480_dst_{}.yuv'.format(count), row, col, framenum,
                targetfrm)
    elif video_type == 10:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/PartyScene_832x480_ref.yuv', row, col, framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/PartyScene_832x480_dst_0{}.yuv'.format(count), row,
                col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/PartyScene_832x480_dst_{}.yuv'.format(count), row,
                col, framenum,
                targetfrm)
    elif video_type == 11:
        if count == 0:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Timelapse_832x480_ref.yuv', row, col,
                framenum,
                targetfrm)
        elif count < 10:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Timelapse_832x480_dst_0{}.yuv'.format(count), row,
                col, framenum,
                targetfrm)
        else:
            temp[0, 0:framenum, :, :, :] = ry420.read_YUV420(
                'D:/csiq video database/Timelapse_832x480_dst_{}.yuv'.format(count), row,
                col, framenum,
                targetfrm)

    return temp
