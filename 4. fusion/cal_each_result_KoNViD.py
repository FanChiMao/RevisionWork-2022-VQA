import numpy as np
from scipy.stats.stats import pearsonr, spearmanr
import scipy.io as sio
from sklearn.svm import SVR

from sklearn import preprocessing


if __name__ == '__main__':
    from utils.read_dmos import read_KoNViD
    # 'E:/VQA Database/KoNViD_1k/KoNViD_1k_mos_delete_one.csv'
    # 'D:/NCHU/1102/senior paper/VQA_code_Fan/1.extract essential frames/sorted_DMOS_KoNViD_delete_one.csv'
    dmos_path_data = 'D:/NCHU/1102/senior paper/VQA_code_Fan/1.extract essential frames/sorted_DMOS_KoNViD_delete_one.csv'

    # 'D:/NCHU/1102/senior paper/VQA_code_Fan/3.predict scores/checkpoints/KoNViD/result_data.mat'
    # 'D:/NCHU/1102/senior paper/VQA_code_Fan/3.predict scores/checkpoints/KoNViD/result_data_sigmoid_update_epochs_100.mat'
    # 'D:/NCHU/1102/senior paper/VQA_code_Fan/3.predict scores/checkpoints/KoNViD/result_data_sigmoid.mat'
    # 'D:/NCHU/1102/senior paper/VQA_code_Fan/3.predict scores/checkpoints/KoNViD/result_data_epochs_150_iteration_3.mat'
    predict_result = 'D:/NCHU/1102/senior paper/VQA_code_Fan/3.predict scores/checkpoints/KoNViD/result_data_epochs_150_iteration_3.mat'

    # same setup for previous extraction process
    iterations = 3
    data_number = 1199
    feature_number = 7

    print('------ Loading predict results ------')
    predict_result_score = sio.loadmat(predict_result)['predicted_data']
    index = sio.loadmat(predict_result)['label_data']
    output = read_KoNViD(dmos_path_data)  # GT
    r_max_4 = 0
    num_4 = []
    count = 0
    predict_score = np.zeros((iterations, data_number, 1))
    temp_predict_score = np.zeros((iterations, data_number, 1))
    f_r_p_array = np.zeros((iterations, 1))
    f_r_s_array = np.zeros((iterations, 1))
    for j in range(1, feature_number+1):
        for k in range(j + 1, feature_number+1):
            for l in range(k + 1, feature_number+1):
                for m in range(l + 1, feature_number+1):
                    r_p_array = np.zeros((iterations, 1))
                    r_s_array = np.zeros((iterations, 1))
                    for i in range(iterations):
                        sum_score = np.squeeze(
                            predict_result_score[i, :, j:j + 1] +
                            predict_result_score[i, :, k:k + 1] +
                            predict_result_score[i, :, l:l + 1] +
                            predict_result_score[i, :, m:m + 1])
                        # print(sum_score)

                        gt = output[:, 0][index[i].astype(int)]
                        if sum_score != []:
                            r_p_array[i], pval_p = pearsonr(sum_score, gt)
                            r_s_array[i], pval_s = spearmanr(sum_score, gt)
                            temp_predict_score[i, :, 0] = sum_score

                    if (np.median(r_p_array) + np.median(r_s_array)) / 2 > r_max_4:
                        r_max_4 = (np.median(r_p_array) + np.median(r_s_array)) / 2
                        num_4 = [j, k, l, m]
                        p_4 = np.median(r_p_array)
                        s_4 = np.median(r_s_array)
                        predict_score[:, :, 0] = temp_predict_score[:, :, 0]
                        f_r_p_array = r_p_array
                        f_r_s_array = r_s_array
                    count += 1

    p_median_index = np.zeros(2)
    s_median_index = np.zeros(2)
    p_median_index[0] = np.argsort(f_r_p_array[:, 0])[len(f_r_p_array) // 2]
    p_median_index[1] = np.argsort(f_r_p_array[:, 0])[len(f_r_p_array) // 2 - 1]
    p_median_index = p_median_index.astype(int)
    s_median_index[0] = np.argsort(f_r_s_array[:, 0])[len(f_r_s_array) // 2]
    s_median_index[1] = np.argsort(f_r_s_array[:, 0])[len(f_r_s_array) // 2 - 1]
    s_median_index = s_median_index.astype(int)

    p = s = 0
    space = []
    space_d = []
    # for i in range(data_number):
    #     space.append(predict_score[p_median_index[U_L], i, 0])
    #     space_d.append(output[:, 0][index[p_median_index[U_L], i].astype(int)])

    for P_S in range(2):
        if P_S == 0:
            for U_L in range(2):
                space = []
                space_d = []
                for i in range(data_number):
                    space.append(predict_score[p_median_index[U_L], i, 0])
                    space_d.append(output[:, 0][index[p_median_index[U_L], i].astype(int)])
                p += pearsonr(space, space_d)[0]
        else:
            for U_L in range(2):
                space = []
                space_d = []
                for i in range(data_number):
                    space.append(predict_score[s_median_index[U_L], i, 0])
                    space_d.append(output[:, 0][index[s_median_index[U_L], i].astype(int)])
                s += pearsonr(space, space_d)[0]

    print('The combination is {}'.format(num_4))
    print('PCC of KoNVid is {}'.format(p / 2))
    print('SROCC of KoNVid is {}'.format(s / 2))



