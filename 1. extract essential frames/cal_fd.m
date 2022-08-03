function temp = cal_fd(data,framenumber)
    for i=2:framenumber
        d(:,:,i-1) = rgb2gray(im2double(data(i).cdata)) - rgb2gray(im2double(data(i-1).cdata));
        a = d(:,:,i-1);
        a_std(i-1)=abs(std(a(:)));
    end
    temp = abs(a_std);
end