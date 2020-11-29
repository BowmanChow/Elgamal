clear all; clc;
msg_len = 1000;
message = randi([0,1], 1, msg_len);
sec_file = 'secrete_key';
pub_file = 'public_key';
msg_file = 'message_to_send.txt';
enc_sen_file = 'encrypted_send.txt';
enc_rec_file = 'encrypted_recieve.txt';
msg_rec = 'message_recieve.txt';
python_cmd = 'python3';
enc_bit_len = 54;

f_msg = fopen(msg_file, 'w');
fprintf(f_msg, '%d', message);
fclose(f_msg);

system([python_cmd,' -c "from Elgamal_file import *; Elgamal_gen_key_file(''',sec_file,''',''',pub_file,''')" '])

system([python_cmd,' -c "from Elgamal_file import *; Elgamal_encrypt_file(''',msg_file,''',''',pub_file,''',''',enc_sen_file,''')" '])

encrypted = send_encrypted(enc_sen_file);

recieve_encrypted(encrypted, enc_rec_file, enc_bit_len);

system([python_cmd,' -c "from Elgamal_file import *; Elgamal_decrypt_file(''',enc_rec_file,''',''',sec_file,''',''',pub_file,''',''',msg_rec,''')" '])

msg_rec = textread(msg_rec,'%s');
msg_rec = msg_rec{1};

msg_char = num2str(message);
msg_char = strrep(msg_char, ' ', '');

error_bit = sum(msg_char ~= msg_rec);

