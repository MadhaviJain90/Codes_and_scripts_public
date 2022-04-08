a=imread('lena_original1.tif');
b=imread('lena_corrupted.tif');
c=imread('3mean_lena_mosaicked.tif');
d=imread('3median_lena_mosaicked.tif');
e=imread('3leesigma_lena_mosaicked.tif');
f=imread('3local_lena_mosaicked.tif');
g=imread('3lee_lena_mosaicked.tif');
h=imread('3frost_lena_mosaicked.tif');
i=imread('3gamma_lena_mosaicked.tif');
j=imread('3open_lena_mosaicked.tif');
k=imread('3close_lena_mosaicked.tif');
l=imread('3erode_lena_mosaicked.tif');
m=imread('3dilate_lena_mosaicked.tif');
n=imread('3lowpass_lena_mosaicked.tif');
o=imread('3highpass_lena_mosaicked.tif');
figure(1),imhist(a)
hold on
figure(1),imhist(b)
hold on
figure(1),imhist(c)
hold on
figure(1),imhist(d)
hold on
figure(1),imhist(e)
hold on
figure(1),imhist(f)
hold on
figure(1),imhist(g)
hold on
figure(1),imhist(h)
hold on
figure(1),imhist(i)
hold on
figure(1),imhist(j)
hold on
figure(1),imhist(k)
hold on
figure(1),imhist(l)
hold on
figure(1),imhist(m)
hold on
figure(1),imhist(n)
hold on
figure(1),imhist(o),legend ('Original Lena Image (shaded)', 'Corrupted Lena Image', '3x3 Mean Filter', '3x3 Median Filter', '3x3 Lee-Sigma Filter', '3x3 Local Region Filter', '3x3 Lee Filter', '3x3 Frost Filter', '3x3 Gamma-MAP Filter', '3x3 Open Morphological Filter', '3x3 Close Morphological Filter', '3x3 Erode Morphological Filter', '3x3 Dilate Morphological Filter', '3x3 Low Pass Filter', '3x3 High Pass Filter');
hold off