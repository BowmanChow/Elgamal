function y = recieve_encrypted(input, file, bit_len)


encrypted_rec = reshape(input, bit_len, [])';
f_enc = fopen(file, 'w');
for i = 1:size(encrypted_rec,1)
    fprintf(f_enc, '%s  ', encrypted_rec(i,:));
    if mod(i,2) == 0
        fprintf(f_enc, '\n');
    end
end
fclose(f_enc)