import numpy as np
import cv2


def read_YUV420(image_path, rows, cols, numfrm, targetfrm):
    gray = np.zeros((rows, cols), np.uint8)
    img_U = np.zeros((int(rows / 2), int(cols / 2)), np.uint8)
    img_V = np.zeros((int(rows / 2), int(cols / 2)), np.uint8)
    result = np.zeros((numfrm, rows, cols, 3), dtype=np.uint8)
    # count = 0
    with open(image_path, 'rb') as reader:
        for k in range(numfrm):
            # if count == targetfrm:
            #     break
            # if (numfrm // (targetfrm - 1)) * count + 0 != k:
            #     reader.seek(int(rows * cols * 1.5), 1)
            #     continue
            for i in range(rows):
                for j in range(cols):
                    gray[i, j] = ord(reader.read(1))
            # reader.seek(int(rows * cols * 0.5), 1)
            for i in range(int(rows / 2)):
                for j in range(int(cols / 2)):
                    img_U[i, j] = ord(reader.read(1))

            for i in range(int(rows / 2)):
                for j in range(int(cols / 2)):
                    img_V[i, j] = ord(reader.read(1))
            # Y分量图像比U、V分量图像大一倍，想要合并3个分量，需要先放大U、V分量和Y分量一样大小
            enlarge_U = cv2.resize(img_U, (0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
            enlarge_V = cv2.resize(img_V, (0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

            # 合并YUV3通道
            img_YUV = cv2.merge([gray, enlarge_U, enlarge_V])
            dst = cv2.cvtColor(img_YUV, cv2.COLOR_YUV2BGR)
            result[k, :, :, 0] = dst[:, :, 0]
            result[k, :, :, 1] = dst[:, :, 1]
            result[k, :, :, 2] = dst[:, :, 2]
            # result[k, :, :, 0] = cv2.resize(dst[:, :, 0], (247, 139))
            # result[k, :, :, 1] = cv2.resize(dst[:, :, 1], (247, 139))
            # result[k, :, :, 2] = cv2.resize(dst[:, :, 2], (247, 139))
            # temp = cv2.resize(gray, (76, 43))
            # result[count, :, :, 0] = temp
            # count = count + 1
        return result
