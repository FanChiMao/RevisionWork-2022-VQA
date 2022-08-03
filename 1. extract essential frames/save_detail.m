clc
clear
close all
%% Set the root and parameters
path_video = 'F:\VQA Database\KoNViD_1k\KoNViD_1k_videos\';
video_list_yuv = dir(strcat(path_video,'*.yuv'));
video_list_mp4 = dir(strcat(path_video,'*.mp4'));
extractedframe = 60;
result = [];
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
    extracted_frames(j,:) = [str2num(video_yuv(1:end-4)), frame_number, width, height] ;   
    fprintf('---------------------------------------\n');
end
xlswrite(['frames_details_' 'KoNViD.xlsx'], extracted_frames);