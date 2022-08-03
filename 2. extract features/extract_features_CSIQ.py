import numpy as np
from keras.applications import Xception
np.random.seed(1337)  # for reproducibility
from keras import Input
from keras.layers import GlobalAveragePooling2D
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model
# import pandas as pd
import read_CSIQ_database as rl
import scipy.io as sio
from keras import backend as K
import readexcel as re


framenum = 600
extracted_frame_num = 60

# 讀取特定幀的資料
frame_index = re.read2('extract_frame_num4_without_low_value_{}_CSIQ.xlsx'.format(extracted_frame_num))
frame_index = np.array(frame_index)
frame_index = frame_index - 1
frame_index_row_t = re.read2('extract_frame_num_row_t_ave_{}_CSIQ.xlsx'.format(extracted_frame_num))
frame_index_row_t = np.array(frame_index_row_t)
frame_index_row_t = frame_index_row_t - 1
frame_index_col_t = re.read2('extract_frame_num_col_t_ave_{}_CSIQ.xlsx'.format(extracted_frame_num))
frame_index_col_t = np.array(frame_index_col_t)
frame_index_col_t = frame_index_col_t - 1


def generate_model(row, col):
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(row, col, 3))
    hidden_layer = base_model.get_layer('mixed4').output
    output_model = GlobalAveragePooling2D()(hidden_layer)
    model = Model(inputs=base_model.input, outputs=output_model)
    return model


# 取spatial frame的CNN
# model = generate_model(480, 832)
model = generate_model(540, 960)
extracted_features = np.zeros((1200, extracted_frame_num, model.output.shape.dims[1].value), dtype=np.float32) #第三個維度會隨著層數的改變而有差別，如最後一層的特徵為2048，倒數第7層為768
# extracted_features_row_t = np.zeros((216, extracted_frame_num, model.output.shape.dims[1].value), dtype=np.float32)
# extracted_features_col_t = np.zeros((216, extracted_frame_num, model.output.shape.dims[1].value), dtype=np.float32)

count = 0
count2 = 0
vtype = 0
for i in range(228):
    sequence = []
    if i == 0:
        vtype = 0
        count = i
        framenum = 600
    elif i == 19:
        vtype = 1
        count = i
        framenum = 600
    elif i == 38:
        vtype = 2
        count = i
        framenum = 500
    elif i == 57:
        vtype = 3
        count = i
        framenum = 500
    elif i == 76:
        vtype = 4
        count = i
        framenum = 250
    elif i == 95:
        vtype = 5
        count = i
        framenum = 240
    elif i == 114:
        vtype = 6
        count = i
        framenum = 300
    elif i == 133:
        vtype = 7
        count = i
        framenum = 300
    elif i == 152:
        vtype = 8
        count = i
        framenum = 240
    elif i == 171:
        vtype = 9
        count = i
        framenum = 240
    elif i == 190:
        vtype = 10
        count = i
        framenum = 500
    elif i == 209:
        vtype = 11
        count = i
        framenum = 300
    if i - count == 0:
        continue
    g = rl.readvideo(0, vtype, i - count)
    g = g.astype('float32')
    print(count2)
    # model = generate_model(framenum, 480)
    # for cols in range(extracted_frame_num):
    #     x = preprocess_input(g[0, :, :, frame_index_row_t[0, cols, 0]])
    #     x = np.expand_dims(x, axis=0)
    #     features = model.predict(x)
    #     sequence.append(features[0])
    # extracted_features_row_t[count2] = np.array(sequence)
    # sequence = []
    # del model
    # K.clear_session()
    # model = generate_model(framenum, 832)
    # for rows in range(extracted_frame_num):
    #     x = preprocess_input(g[0, :, frame_index_col_t[0, rows, 0], :])
    #     x = np.expand_dims(x, axis=0)
    #     features = model.predict(x)
    #     sequence.append(features[0])
    # extracted_features_col_t[count2] = np.array(sequence)
    # sequence = []
    # del model
    # K.clear_session()
    # count2 = count2 + 1
# sio.savemat('extracted_features_row_t_previous6_pool_layer_CSIQ.mat', {'0': extracted_features_row_t[0:18], '1': extracted_features_row_t[18:36], '2':
#     extracted_features_row_t[36:54], '3': extracted_features_row_t[54:72], '4': extracted_features_row_t[72:90], '5':
#     extracted_features_row_t[90:108], '6': extracted_features_row_t[108:126], '7': extracted_features_row_t[126:144], '8':
#     extracted_features_row_t[144:162], '9': extracted_features_row_t[162:180], '10': extracted_features_row_t[180:198], '11': extracted_features_row_t[198:216]})
# sio.savemat('extracted_features_col_t_previous6_pool_layer_CSIQ.mat', {'0': extracted_features_col_t[0:18], '1': extracted_features_col_t[18:36], '2':
#     extracted_features_col_t[36:54], '3': extracted_features_col_t[54:72], '4': extracted_features_col_t[72:90], '5':
#     extracted_features_col_t[90:108], '6': extracted_features_col_t[108:126], '7': extracted_features_col_t[126:144], '8':
#     extracted_features_col_t[144:162], '9': extracted_features_col_t[162:180], '10': extracted_features_col_t[180:198], '11': extracted_features_col_t[198:216]})
    for frame in range(extracted_frame_num):
        x = preprocess_input(g[0, frame_index[0, i, frame]])
        x = np.expand_dims(x, axis=0)
        features = model.predict(x)
        sequence.append(features[0])
    extracted_features[count2, 0:extracted_frame_num, :] = np.array(sequence)
    sequence = []
    count2 = count2 + 1
sio.savemat('extracted_features_previous6_pool_layer_CSIQ.mat', {'0': extracted_features[0:18], '1': extracted_features[18:36], '2':
    extracted_features[36:54], '3': extracted_features[54:72], '4': extracted_features[72:90], '5':
    extracted_features[90:108], '6': extracted_features[108:126], '7': extracted_features[126:144], '8':
    extracted_features[144:162], '9': extracted_features[162:180], '10': extracted_features[180:198], '11': extracted_features[198:216]})


