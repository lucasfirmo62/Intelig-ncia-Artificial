%colocar dentro da pasta Train para pegar dados do Treino
images = dir("*.bmp");

fid = fopen('treino.txt', 'w');
for i=1:size(images)
    [img, map] = imread(fullfile(images(i).name)) ;

    [img, map] = ind2rgb(img, map);

    [img, map] = imresize([img, map],[256 256]);

    imageMP = [img, map];
    
    if fid == -1, error('Cannot open file'); end

    if i < 81
        imageMP = imcrop(imageMP, [64 64 160 128]);
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '0\n');
    elseif i < 140 && i > 80
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '1\n');
    elseif i < 173 && i > 139
        imageMP = imcrop(imageMP, [64 64 160 128]);
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '2\n');
    elseif i < 203 && i > 172
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '3\n');
    elseif i > 202
        imageMP = imcrop(imageMP, [0 0 256 80]);
        imageMP = imresize(imageMP,[256 256]);
        fprintf(fid, '%f ', imageMP);
        fprintf(fid, '4\n');
    end
end
fclose(fid);