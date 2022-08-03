import numpy as np
from keras.applications import Xception

np.random.seed(1337)  # for reproducibility
from keras import Input
from keras.layers import GlobalAveragePooling2D
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model
# import pandas as pd
import read_database as rd
import scipy.io as sio
from keras import backend as K
import readexcel as re

extracted_frame_num = 60
video_dir = 'F:/VQA Database/KoNViD_1k/KoNViD_1k_videos'

# 讀取特定幀的資料
frame_index = re.read2(
    '../1.extract essential frames/extract_frame_num4_without_low_value_{}_KoNViD_1k_test.xlsx'.format(extracted_frame_num))
frame_index = np.array(frame_index)
frame_index = frame_index - 1
frame_index_row_t = re.read2(
    '../1.extract essential frames/extract_frame_num_row_t_ave_{}_KoNViD_1k.xlsx'.format(extracted_frame_num))
frame_index_row_t = np.array(frame_index_row_t)
frame_index_row_t = frame_index_row_t - 1
frame_index_col_t = re.read2(
    '../1.extract essential frames/extract_frame_num_col_t_ave_{}_KoNViD_1k.xlsx'.format(extracted_frame_num))
frame_index_col_t = np.array(frame_index_col_t)
frame_index_col_t = frame_index_col_t - 1
frame_detail = re.read2('../1.extract essential frames/frames_details_KoNViD_1k_test.xlsx')
frame_detail = np.array(frame_detail)

def generate_model(row, col):
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(row, col, 3))
    hidden_layer = base_model.get_layer('mixed9').output
    output_model = GlobalAveragePooling2D()(hidden_layer)
    model = Model(inputs=base_model.input, outputs=output_model)
    return model


# 取spatial frame的CNN
model = generate_model(540, 960)
extracted_features = np.zeros((1199, extracted_frame_num, model.output.shape.dims[1].value),dtype=np.float32)
# 第三個維度會隨著層數的改變而有差別，如最後一層的特徵為2048，倒數第7層為768

extracted_features_row_t = np.zeros((1199, extracted_frame_num, model.output.shape.dims[1].value), dtype=np.float32)
# extracted_features_col_t = np.zeros((1199, extracted_frame_num, model.output.shape.dims[1].value), dtype=np.float32)

video_num = len(frame_detail[0])

for i in range(0, video_num):
    sequence = []
    g, framenum, width, height = rd.readvideo(0, video_dir, frame_detail[0][i])
    g = g.astype('float32')
    print('({}/{}) video name: {}'.format(i + 1, video_num, frame_detail[0][i][0]))

    model = generate_model(framenum, height)
    for cols in range(extracted_frame_num):
        x = preprocess_input(g[0, :, :, frame_index_row_t[0, cols, 0]])
        x = np.expand_dims(x, axis=0)
        features = model.predict(x)
        sequence.append(features[0])
    extracted_features_row_t[i] = np.array(sequence)
    sequence = []
    del model
    K.clear_session()
sio.savemat('./extracted_features_row_t_previous_pool_layer_KoNViD_1k.mat', {'0': extracted_features_row_t[:]})
# sio.savemat('./extracted_features_rol_t_ave_60_KoNViD_1k.mat', {'0': extracted_features_row_t[:]})

    # model = generate_model(framenum, width)
    # for rows in range(extracted_frame_num):
    #     x = preprocess_input(g[0, :, frame_index_col_t[0, rows, 0], :])
    #     x = np.expand_dims(x, axis=0)
    #     features = model.predict(x)
    #     sequence.append(features[0])
    # extracted_features_col_t[i] = np.array(sequence)
    # sequence = []
    # del model
    # K.clear_session()
# sio.savemat('./extracted_features_col_t_ave_60_KoNViD_1k.mat', {'0': extracted_features_col_t[:]})

#     for frame in range(extracted_frame_num):
#         x = preprocess_input(g[0, frame_index[0, i, frame]])
#         x = np.expand_dims(x, axis=0)
#         features = model.predict(x)
#         sequence.append(features[0])
#     extracted_features[i, 0:extracted_frame_num, :] = np.array(sequence)
#     sequence = []
# sio.savemat('./extracted_features_without_low_value_KoNViD_1k.mat', {'0': extracted_features[:]})
# sio.savemat('./extracted_features_previous_pool_layer_KoNViD_1k.mat', {'0': extracted_features[:]})