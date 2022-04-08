a=imread('LE70410362003034EDC00_B6_VCID_2.tif');
b=imread('3feb2003_gap_mask_noisy_construct.tif');
c=imread('3median_losangeles_mosaicked.tif');
d=imread('3local_losangeles_mosaicked.tif');
e=imread('3open_losangeles_mosaicked.tif');
f=imread('3close_losangeles_mosaicked.tif');
g=imread('3erode_losangeles_mosaicked.tif');
h=imread('3dilate_losangeles_mosaicked.tif');
figure(4),imhist(a)
hold on
figure(4),imhist(b)
hold on
figure(4),imhist(c)
hold on
figure(4),imhist(d)
hold on
figure(4),imhist(e)
hold on
figure(4),imhist(f)
hold on
figure(4),imhist(g)
hold on
figure(4),imhist(h),legend ('Original Landsat Image (shaded)', 'Corrupted Landsat Image', '3x3 Median Filter', '3x3 Local Region Filter', '3x3 Open Morphological Filter', '3x3 Close Morphological Filter', '3x3 Erode Morphological Filter', '3x3 Dilate Morphological Filter');
hold off