clc
clear
close all
%% Set the root and parameters
path_video = 'E:\VQA Database\KoNViD_1k\KoNViD_1k_videos\';
video_list_yuv = dir(strcat(path_video,'*.yuv'));
data = readtable('E:/VQA Database/KoNViD_1k/KoNViD_1k_mos_delete_one.csv');
data = table2array(data);
extractedframe = 60;
video_num = length(video_list_yuv);
for j = 1:video_num
    video_yuv = video_list_yuv(j).name;
    video_name = str2num(video_yuv(1:end-4));
    indices = find(data(:,1) == video_name);
    dmos = data(indices,2);
    fprintf('%d, %f\n', indices, dmos);
    extracted_frames(j,:) = [video_name, dmos] ;   
    fprintf('---------------------------------------\n');
end
xlswrite(['sorted_DMOS_KoNViD.xlsx'], extracted_frames);