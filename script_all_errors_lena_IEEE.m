%read two images
A = imread('lena_original1.tif');
B = imread('29gamma_lena.tif');
%convert to double(ie value range from 0 to 1 instead of 0 to 255)
C = im2double(A);
D = im2double(B);
%calculate normalized histogram of images
hn1 = imhist(C)./numel(C);
hn2 = imhist(D)./numel(D);
%calculate the histogram error
HE = sum((hn1-hn2).^2)

err = C-D;
err = err.^2;
err = sum(err(:));
err = err/(512*512);
RMSE = sqrt(err)

PSNR = psnr(C,D)

SSIM = ssim(C,D)