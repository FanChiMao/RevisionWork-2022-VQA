clc;clear all;close all;
width            = 832;
height           = 480;
extractedframe = 60;
framenumber = 600;
opticFlow = opticalFlowLK('NoiseThreshold',0.009);
temp2 = [];
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\BQMall_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        [mov,imgRgb] = loadFileYuv(['D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0' num2str(i-1) '.yuv'], width, height, 1:framenumber);
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
        fprintf('frames number: %d\n', length(mov));
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
    fprintf('%d\n', i);
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\BQMall_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
BQMall = [temp2];
%%
temp2 = [];
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\BQTerrace_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\BQTerrace_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\BQTerrace_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
BQTerrace = [temp2];
%%
temp2 = [];
framenumber = 500;
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\BasketballDrive_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\BasketballDrive_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\BasketballDrive_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
BasketballDrive = temp2;
%%
temp2 = [];
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Cactus_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Cactus_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Cactus_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
Cactus = temp2;
%%
temp2 = [];
framenumber = 250;
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Carving_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Carving_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Carving_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
Carving = temp2;
%%
temp2 = [];
framenumber = 240;
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Chipmunks_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Chipmunks_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Chipmunks_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
Chipmunks = temp2;
%%
temp2 = [];
framenumber = 300;
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Flowervase_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Flowervase_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Flowervase_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
Flowervase = temp2;
%%
temp2 = [];
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Keiba_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Keiba_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Keiba_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
Keiba = temp2;
%%
temp2 = [];
framenumber = 240;
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Kimono_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Kimono_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Kimono_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
Kimono = temp2;
%%
temp2 = [];
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\ParkScene_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\ParkScene_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\ParkScene_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
ParkScene = temp2;
%%
temp2 = [];
framenumber = 500;
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\PartyScene_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\PartyScene_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\PartyScene_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
PartyScene = temp2;
%%
temp2 = [];
framenumber = 300;
for i=2:10
    if i==1
        eval(['[mov,imgRgb] = loadFileYuv(''D:\database\csiq video database\Timelapse_832x480_ref.yuv'', width, height, 1:framenumber);']);
    else
        eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Timelapse_832x480_dst_0' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    end
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
for i=11:19
	eval(['[mov,imgRgb] = loadFileYuv(''D:\NCHU\1102\學長期刊\VQA_chu\dataset\csiq video database\dst\BQMall_832x480_dst_0\Timelapse_832x480_dst_' num2str(i-1) '.yuv'', width, height, 1:framenumber);']);
    temp = [];
    fd = cal_fd(mov,framenumber);
    temp = 1./fd;
    [sorted, index]=sort(temp);
    [sorted_, index_]=sort(index(1:extractedframe));
    temp2(i-1,:) = sorted_+1;
end
Timelapse = temp2;
temp2 = [];

a=[BQMall; BQTerrace; BasketballDrive; Cactus; Carving; Chipmunks; Flowervase; Keiba; Kimono; ParkScene; PartyScene; Timelapse];
xlswrite(['extract_frame_num4_without_low_value_' int2str(extractedframe) '_CSIQ.xlsx'], a);

