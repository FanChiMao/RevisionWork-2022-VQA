from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, concatenate, BatchNormalization, GlobalMaxPooling1D
# from keras.optimizers import Adam
from tensorflow.keras.optimizers import Adam # - Works
from tensorflow.keras import backend as K, Input
import tensorflow as tf

def generate_model_3():
    minput1 = Input(shape=(60, 2048))
    model1_nor = BatchNormalization()(minput1)
    model1 = GlobalMaxPooling1D()(model1_nor)
    minput2 = Input(shape=(60, 2048))
    model2_nor = BatchNormalization()(minput2)
    model2 = GlobalMaxPooling1D()(model2_nor)
    minput3 = Input(shape=(60, 2048))
    model3_nor = BatchNormalization()(minput3)
    model3 = GlobalMaxPooling1D()(model3_nor)
    merged1 = concatenate([model1, model2, model3])
    model4 = BatchNormalization()(merged1)
    model4 = Dense(1024, activation='relu')(model4)
    model4_output = Dense(1)(model4)  # 123
    main_model = Model(inputs=[minput1, minput2, minput3], outputs=[model4_output])
    optimizer = Adam(lr=1e-5)
    main_model.compile(loss=correlation_loss(), optimizer=optimizer)
    # main_model.summary()
    return main_model


def generate_model_3_previous2():
    minput1 = Input(shape=(60, 1280))
    model1_nor = BatchNormalization()(minput1)
    model1 = GlobalMaxPooling1D()(model1_nor)
    minput2 = Input(shape=(60, 1280))
    model2_nor = BatchNormalization()(minput2)
    model2 = GlobalMaxPooling1D()(model2_nor)
    minput3 = Input(shape=(60, 1280))
    model3_nor = BatchNormalization()(minput3)
    model3 = GlobalMaxPooling1D()(model3_nor)
    merged1 = concatenate([model1, model2, model3])
    model4 = BatchNormalization()(merged1)
    model4 = Dense(640, activation='relu')(model4)
    model4_output = Dense(1)(model4)  # 123
    main_model = Model(inputs=[minput1, minput2, minput3], outputs=[model4_output])
    optimizer = Adam(lr=1e-5)
    main_model.compile(loss=correlation_loss(), optimizer=optimizer)
    # main_model.summary()
    return main_model


def generate_model_3_previous3_4():
    minput1 = Input(shape=(60, 768))
    model1_nor = BatchNormalization()(minput1)
    model1 = GlobalMaxPooling1D()(model1_nor)
    minput2 = Input(shape=(60, 768))
    model2_nor = BatchNormalization()(minput2)
    model2 = GlobalMaxPooling1D()(model2_nor)
    minput3 = Input(shape=(60, 768))
    model3_nor = BatchNormalization()(minput3)
    model3 = GlobalMaxPooling1D()(model3_nor)
    merged1 = concatenate([model1, model2, model3])
    model4 = BatchNormalization()(merged1)
    model4 = Dense(384, activation='relu')(model4)
    model4_output = Dense(1)(model4)  # 123
    main_model = Model(inputs=[minput1, minput2, minput3], outputs=[model4_output])
    optimizer = Adam(lr=1e-5)
    main_model.compile(loss=correlation_loss(), optimizer=optimizer)
    # main_model.summary()
    return main_model

def correlation_loss():
    def correlation_coefficient_loss(y_true, y_pred):
        x = y_true
        y = y_pred
        mx = K.mean(x)
        my = K.mean(y)
        xm, ym = x - mx, y - my
        r_num = K.sum(tf.multiply(xm, ym))
        r_den = K.sqrt(tf.multiply(K.sum(K.square(xm)), K.sum(K.square(ym))))
        r = r_num / r_den
        r = K.maximum(K.minimum(r, 1.0), -1.0)
        y_true_ = (y_true - K.min(y_true)) / (K.max(y_true) - K.min(y_true))
        y_pred_ = (y_pred - K.min(y_pred)) / (K.max(y_pred) - K.min(y_pred))
        return (1 - K.square(r)) * 1 + 1 * K.mean(K.square(y_pred_ - y_true_), axis=-1) + 0.01 * K.mean(
            K.abs(y_pred - y_true), axis=-1)

    return correlation_coefficient_loss


def each_layer_info(channel, feature):
    if channel == 3:  # mix10
        key_row = '_row_t_ave_60_'
        key_col = '_col_t_ave_60_'
        key_spatial = '_s_ave_60_'
        model = generate_model_3()
    elif channel == 4:  # mix9
        key_row = '_row_t_previous_'
        key_col = '_col_t_previous_'
        key_spatial = '_s_previous_'
        model = generate_model_3()
    elif channel == 5:  # mix8
        key_row = '_row_t_previous2_'
        key_col = '_col_t_previous2_'
        key_spatial = '_s_previous2_'
        model = generate_model_3_previous2()
    elif channel == 6:  # mix7
        key_row = '_row_t_previous3_'
        key_col = '_col_t_previous3_'
        key_spatial = '_s_previous3_'
        model = generate_model_3_previous3_4()
    elif channel == 7:  # mix6
        key_row = '_row_t_previous4_'
        key_col = '_col_t_previous4_'
        key_spatial = '_s_previous4_'
        model = generate_model_3_previous3_4()
    elif channel == 8:  # mix5
        key_row = '_row_t_previous5_'
        key_col = '_col_t_previous5_'
        key_spatial = '_s_previous5_'
        model = generate_model_3_previous3_4()
    elif channel == 9:  # mix4
        key_row = '_row_t_previous6_'
        key_col = '_col_t_previous6_'
        key_spatial = '_s_previous6_'
        model = generate_model_3_previous3_4()

    for index, file_name in enumerate(feature):
        if key_row in file_name:
            index_row = index
        if key_col in file_name:
            index_col = index
        if key_spatial in file_name:
            index_spatial = index

    return model, [index_row, index_col, index_spatial]

# def each_layer_info(channel, feature):
#     if channel == 0:  # mix10
#         key_row = '_row_t_ave_60_'
#         key_col = '_col_t_ave_60_'
#         key_spatial = '_s_ave_60_'
#         model = generate_model_3()
#     elif channel == 1:  # mix9
#         key_row = '_row_t_previous_'
#         key_col = '_col_t_previous_'
#         key_spatial = '_s_previous_'
#         model = generate_model_3()
#     elif channel == 2:  # mix8
#         key_row = '_row_t_previous2_'
#         key_col = '_col_t_previous2_'
#         key_spatial = '_s_previous2_'
#         model = generate_model_3_previous2()
#     elif channel == 3:  # mix7
#         key_row = '_row_t_previous3_'
#         key_col = '_col_t_previous3_'
#         key_spatial = '_s_previous3_'
#         model = generate_model_3_previous3_4()
#     elif channel == 4:  # mix6
#         key_row = '_row_t_previous4_'
#         key_col = '_col_t_previous4_'
#         key_spatial = '_s_previous4_'
#         model = generate_model_3_previous3_4()
#     elif channel == 5:  # mix5
#         key_row = '_row_t_previous5_'
#         key_col = '_col_t_previous5_'
#         key_spatial = '_s_previous5_'
#         model = generate_model_3_previous3_4()
#     elif channel == 6:  # mix4
#         key_row = '_row_t_previous6_'
#         key_col = '_col_t_previous6_'
#         key_spatial = '_s_previous6_'
#         model = generate_model_3_previous3_4()
#
#     for index, file_name in enumerate(feature):
#         if key_row in file_name:
#             index_row = index
#         if key_col in file_name:
#             index_col = index
#         if key_spatial in file_name:
#             index_spatial = index
#
#     return model, [index_row, index_col, index_spatial]

if __name__ == '__main__':
    from utils.read_dmos import read_KoNViD
    import scipy.io as sio
    import numpy as np
    import os
    from natsort import natsorted
    from glob import glob

    features_path = 'D:/NCHU/1102/senior paper/VQA_code_Fan/2.extract features/'
    dmos_path_data = 'F:/VQA Database/KoNViD_1k/KoNViD_1k_mos_delete_one.csv'
    files = natsorted(glob(os.path.join(features_path, '*.mat')))
    all_data = []

    corresponding_file = []
    for each in files:
        data_temp = sio.loadmat(each)
        data_temp = np.array(data_temp['0'])
        all_data.append(data_temp)
        corresponding_file.append(each)

    for channel in range(3, 10):
        model, [r, c, s] = each_layer_info(channel=channel, feature=corresponding_file)
        print('channel: {} --> [{}, {}, {}]'.format(channel, r, c, s))






