clc;clear all;close all;
% 解析度
width            = 960;
height           = 540;
% 取幀的數目
extractedframe = 60;
frame_interval_row_t = floor(width/extractedframe);
frame_interval_col_t = floor(height/extractedframe);
extract_frame_num_row_t = [];
extract_frame_num_col_t = [];
for i=1:extractedframe
    extract_frame_num_row_t = [extract_frame_num_row_t 1+(i-1)*frame_interval_row_t];
    extract_frame_num_col_t = [extract_frame_num_col_t 1+(i-1)*frame_interval_col_t];
end
xlswrite(['extract_frame_num_row_t_ave_' int2str(extractedframe) '_KoNViD_1k.xlsx'], extract_frame_num_row_t');
xlswrite(['extract_frame_num_col_t_ave_' int2str(extractedframe) '_KoNViD_1k.xlsx'], extract_frame_num_col_t');