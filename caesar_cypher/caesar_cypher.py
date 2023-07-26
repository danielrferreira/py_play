#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import string as st

wd = input('Enter the directory that your txt file is: ' )

os.chdir(wd)

file_name = input('Enter the name of the file, include .txt at the end: ')

with open(file_name, 'r') as file:
    input_str = file.read()
    
offset = int(input('Enter the offset. (eg. 1 if A should be translated to B):'))

letters = list(st.ascii_lowercase)

enc_letters_1 = ['']*(26-offset)

enc_letters_2 = ['']*offset

for i in range(0,(26-offset)):
    enc_letters_1[i] = chr(ord(letters[i])+offset)
    
for i in range(0,offset):    
    enc_letters_2[i] = letters[i]

enc_letters = enc_letters_1 + enc_letters_2

ENC_LETTERS = [char.upper() for char in enc_letters]
LETTERS = [char.upper() for char in letters]

all_letters = letters + LETTERS
all_enc_letters = enc_letters + ENC_LETTERS

del wd, letters, LETTERS, enc_letters_1, enc_letters_2, enc_letters, ENC_LETTERS

result = ''

for j in input_str:
    if j in all_letters:
        for k in range(0,52):
            if j==all_enc_letters[k]:
                result_letter = all_letters[k]
    else:
        result_letter=j
    
    result += result_letter
    
with open('result_text.txt', 'w') as file:
    file.write(result)

print('The result txt should be in the same directory as of your input txt')
