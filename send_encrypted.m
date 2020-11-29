function encrypted = send_encrypted(file)

encrypted = textread(file,'%s');
encrypted = reshape(encrypted,1,[]);
encrypted = cell2mat(encrypted);