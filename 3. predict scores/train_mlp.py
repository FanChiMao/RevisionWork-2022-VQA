import os.path
from natsort import natsorted
from glob import glob
import numpy as np
from numpy import inf

np.random.seed(1337)  # for reproducibility

from scipy.stats.stats import pearsonr, spearmanr
from tensorflow.keras import backend as K, Input
import scipy.io as sio

if __name__ == '__main__':
    from utils.read_dmos import read_KoNViD
    from utils.different_layer import each_layer_info

    features_path = 'D:/NCHU/1102/senior paper/VQA_code_Fan/2.extract features/'
    dmos_path_data = 'D:/NCHU/1102/senior paper/VQA_code_Fan/1.extract essential frames/sorted_DMOS_KoNViD_delete_one.csv'
    files = natsorted(glob(os.path.join(features_path, '*.mat')))
    all_data = []
    corresponding_file = []

    print('------ Reading extracted features -----')
    for each in files:
        data_temp = sio.loadmat(each)
        data_temp = np.array(data_temp['0'])  # np.nan_to_num()
        # data_temp[data_temp == -inf] = 0
        all_data.append(data_temp)
        corresponding_file.append(each)

    iterations = 3
    epochs = 150
    fold_number = 10
    data_number = 1199
    feature_number = 7
    BATCH_SIZE = 1
    data_divide = data_number // fold_number + 1
    vali_data_divide = data_divide - 1

    final_label_data = np.zeros((iterations, data_number))  # random video order
    final_predicted_data = np.zeros((iterations, data_number, feature_number))  # predict score [mix10, 9, 8, ...]
    final_r_p_array = np.zeros((iterations, fold_number + 1, feature_number))  # PLCC result
    final_r_s_array = np.zeros((iterations, fold_number + 1, feature_number))  # SROCC result

    # ground truth (D-MOS)
    print('------ Reading DMOS ground truth ------')
    output = read_KoNViD(dmos_path_data)

    data_shuffle = []

    print('------ Start training -----------------')
    for iteration in range(iterations):
        print('==============Iteration {}=============='.format(iteration + 1))
        index = [i for i in range(data_number)]
        # random number
        np.random.shuffle(index)

        # shuffle the video & label order
        for each_data in all_data:
            data_shuffle.append(each_data[index])
        label_shuffle = output[index]  # <-- ground truth
        final_label_data[iteration] = index

        # training different folds
        for model_ in range(0, fold_number):
            # model_ = 9  # -> debug
            if model_ == 9:  # last fold (把不整除的資料處理掉)
                predict_train_score = np.zeros((961, feature_number))
                predict_test_score = np.zeros((119, feature_number))
                X_train = []
                X_test = []
                for i, each_shuffle_data in enumerate(data_shuffle):
                    X_train.append(np.vstack((each_shuffle_data[0:data_divide * model_], each_shuffle_data[data_divide * (1 + model_) - 1:])))  # data_divide = 120
                    X_test.append((each_shuffle_data[0 + data_divide * model_:data_divide * (1 + model_) - 1]))
                Y_train = np.vstack((label_shuffle[0:data_divide * model_], label_shuffle[data_divide * (1 + model_) - 1:]))
                Y_test = label_shuffle[0 + data_divide * model_:data_divide * (1 + model_) - 1]

            else:
                predict_train_score = np.zeros((960, feature_number))
                predict_test_score = np.zeros((120, feature_number))
                X_train = []
                X_test = []
                for i, each_shuffle_data in enumerate(data_shuffle):
                    X_train.append(np.vstack(
                        (each_shuffle_data[0:data_divide * model_], each_shuffle_data[data_divide * (1 + model_):])))
                    X_test.append((each_shuffle_data[0 + data_divide * model_:data_divide * (1 + model_)]))
                Y_train = np.vstack((label_shuffle[0:data_divide * model_], label_shuffle[data_divide * (1 + model_):]))
                Y_test = label_shuffle[0 + data_divide * model_:data_divide * (1 + model_)]

            Y_train = Y_train[:, 0]
            Y_test = Y_test[:, 0]

            # training different feature layer (mix10 to mix4)
            # mix10, mix9 -> 2048
            # mix8        -> 1280
            # mix7 ~ mix4 -> 768

            for channel in range(3, 10):
                model, [r, c, s] = each_layer_info(channel=channel, feature=corresponding_file)

                r_max = 0
                for epoch in range(epochs):
                    print('==== Iteration {} Model {} Channel {} Epoch {} ===='.format(iteration + 1, model_ + 1,
                                                                                       channel + 1, epoch + 1))
                    history = model.fit(
                        [np.vstack((X_train[r][0:vali_data_divide * (model_ % 9)],
                                    X_train[r][vali_data_divide * (1 + (model_ % 9)):])),
                         np.vstack((X_train[c][0:vali_data_divide * (model_ % 9)],
                                    X_train[c][vali_data_divide * (1 + (model_ % 9)):])),
                         np.vstack((X_train[s][0:vali_data_divide * (model_ % 9)],
                                    X_train[s][vali_data_divide * (1 + (model_ % 9)):]))],
                        [np.hstack(
                            (Y_train[0:vali_data_divide * (model_ % 9)],
                             Y_train[vali_data_divide * (1 + (model_ % 9)):]))],
                        batch_size=BATCH_SIZE,
                        epochs=1,
                        verbose=0)

                    result = model.predict(
                        [np.vstack((X_train[r][0:vali_data_divide * (model_ % 9)],
                                    X_train[r][vali_data_divide * (1 + (model_ % 9)):])),
                         np.vstack((X_train[c][0:vali_data_divide * (model_ % 9)],
                                    X_train[c][vali_data_divide * (1 + (model_ % 9)):])),
                         np.vstack((X_train[s][0:vali_data_divide * (model_ % 9)],
                                    X_train[s][vali_data_divide * (1 + (model_ % 9)):]))],
                        verbose=0)

                    aaa = np.array(result)
                    result = model.predict(
                        [X_train[r][0 + vali_data_divide * (model_ % 9):vali_data_divide * (1 + (model_ % 9))],
                         X_train[c][0 + vali_data_divide * (model_ % 9):vali_data_divide * (1 + (model_ % 9))],
                         X_train[s][0 + vali_data_divide * (model_ % 9):vali_data_divide * (1 + (model_ % 9))]],
                        verbose=0)

                    aa = np.array(result)
                    result = model.predict([X_test[r], X_test[c], X_test[s]], verbose=0)
                    a = np.array(result)

                    r_p__, pval_p = pearsonr(aaa[:, 0], np.hstack(
                        (Y_train[0:vali_data_divide * (model_ % 9)], Y_train[vali_data_divide * (1 + (model_ % 9)):])))
                    r_s__, pval_s = spearmanr(aaa[:, 0], np.hstack(
                        (Y_train[0:vali_data_divide * (model_ % 9)], Y_train[vali_data_divide * (1 + (model_ % 9)):])))
                    r_p_, pval_p = pearsonr(aa[:, 0], Y_train[0 + vali_data_divide * (model_ % 9):vali_data_divide * (
                                1 + (model_ % 9))])
                    r_s_, pval_s = spearmanr(aa[:, 0], Y_train[0 + vali_data_divide * (model_ % 9):vali_data_divide * (
                                1 + (model_ % 9))])
                    r_p, pval_p = pearsonr(a[:, 0], Y_test)
                    r_s, pval_s = spearmanr(a[:, 0], Y_test)

                    #  validate
                    r_mean = (r_p__ + r_s__) / 2 + (r_p_ + r_s_) / 2
                    if r_mean > r_max:
                        r_max = r_mean
                        predict_train_score[:, channel * 1 - 3:(channel + 1) * 1 - 3] = aaa
                        predict_test_score[:, channel * 1 - 3:(channel + 1) * 1 - 3] = a

                del model
                K.clear_session()

            # store the result
            for i in range(feature_number):
                r_p = pearsonr(predict_test_score[:, i], Y_test)[0]
                r_s = spearmanr(predict_test_score[:, i], Y_test)[0]
                final_r_p_array[iteration, model_, i] = r_p
                final_r_s_array[iteration, model_, i] = r_s
                if model_ == 9:
                    final_predicted_data[iteration, 0 + data_divide * model_:data_divide * (1 + model_) - 1,
                    i] = predict_test_score[:, i]
                else:
                    final_predicted_data[iteration, 0 + data_divide * model_:data_divide * (1 + model_),
                    i] = predict_test_score[:, i]

        for i in range(feature_number):
            r_p = pearsonr(final_predicted_data[iteration, :, i], label_shuffle[:, 0])
            r_s = spearmanr(final_predicted_data[iteration, :, i], label_shuffle[:, 0])
            final_r_p_array[iteration, fold_number, 0] = r_p[0]
            final_r_s_array[iteration, fold_number, 0] = r_s[0]

        sio.savemat(
            'checkpoints/KoNViD/result_data_epochs_250_iteration_3.mat',
            {'p': final_r_p_array, 's': final_r_s_array, 'predicted_data': final_predicted_data,
             'label_data': final_label_data})
