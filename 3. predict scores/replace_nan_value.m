clc
clear
close all
%% Parameters
iterations = 3;
feature_number = 7;
%% Main
count=1;
for i=1:iterations
    if(ismember(1,isnan(p(i,:,:))))
        while(ismember(1,isnan(p1(count,:,:))))
            count = count + 1;
        end
        p(i,:,:) = p1(count,:,:);
        s(i,:,:) = p1(count,:,:);
        label_data(i,:) = label_data1(count,:);
        predicted_data(i,:,:) = predicted_data1(count,:,:);
        count = count + 1;
    end
end
for i=1:feature_number
    for j=1:iterations
        p(j,11,i) = corr(predicted_data(j,:,i)',dmos(label_data(j,:)+1));
    end
end
for i=1:feature_number
    for j=1:iterations
        s(j,11,i) = corr(predicted_data(j,:,i)',dmos(label_data(j,:)+1),'type','Spearman');
    end
end