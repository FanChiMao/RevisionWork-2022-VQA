clc
clear
close all
%% Set the root and parameters
path_video = 'F:\VQA Database\KoNViD_1k\KoNViD_1k_videos\';
video_list_yuv = dir(strcat(path_video,'*.yuv'));
video_list_mp4 = dir(strcat(path_video,'*.mp4'));
extractedframe = 60;
extracted_frames = [];
opticFlow = opticalFlowLK('NoiseThreshold',0.009);
fprintf('Start extracting essential frames \n');
video_num = length(video_list_yuv);
for j = 1:video_num
    video_yuv = video_list_yuv(j).name;
    video_mp4 = video_list_mp4(j).name;
    vidObj = VideoReader(strcat(path_video, video_mp4));
    vidFrame = readFrame(vidObj);
    [height, width, channel] = size(vidFrame);
    fprintf('Video: %s (%4d/%4d) \n', video_mp4, j, video_num);
    frame_number = 1;
    while hasFrame(vidObj)
        vidFrame = readFrame(vidObj);
        pause(1/vidObj.FrameRate);
        frame_number = frame_number + 1;
        %fprintf('%d\n', frame_number);
    end
    fprintf('  frame_width  : %d\n', width);
    fprintf('  frame_height : %d\n', height);
    fprintf('  frame_numbers: %d\n', frame_number);
    [mov,imgRgb] = loadFileYuv(strcat(path_video, video_yuv), width, height, 1:frame_number);
    
    temp = [];
    fd = cal_fd(mov,frame_number);
    temp = 1./fd;
    [sorted, index] = sort(temp);
    [sorted_, index_] = sort(index(1:extractedframe));
    extracted_frames(j,:) = sorted_+1;   
    fprintf('---------------------------------------\n');
end
xlswrite(['extract_frame_num4_without_low_value_' int2str(extractedframe) '_KoNViD.xlsx'], extracted_frames);