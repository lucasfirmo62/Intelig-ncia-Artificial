%colocar dentro da pasta Valid para extrair as características
images = dir("*.bmp");

fid = fopen('teste.txt', 'w');
for i=1:size(images)
    [img, map] = imread(fullfile(images(i).name)) ;

    [img, map] = ind2rgb(img, map);

    imageMP = [img, map];

    if fid == -1, error('Cannot open file'); end

    if i < 36
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '0\n');
    elseif i < 61 && i > 35
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '1\n');
    elseif i < 74 && i > 60
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '2\n');
    elseif i < 86 && i > 73
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '3\n');
    elseif i > 85
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '4\n');
    end
end
fclose(fid);