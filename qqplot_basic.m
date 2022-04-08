a = imread('LE70410362003034EDC00_B6_VCID_2.tif');
b = imread('3feb2003_gap_mask_noisy_construct.tif');
c = im2double(a);
d = im2double(b);
figure(1), qqplot(c,d,'+')
hFig = figure(1);
set(hFig, 'Position', [0,0,400,500])
hline = refline(1,0) 
h = findobj('Color','red');
delete(h)
g = findobj('Color','blue');
set(g,'Color','black')