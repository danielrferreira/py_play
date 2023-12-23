#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:06:36 2023

@author: danielferreira
"""

import pandas as pd
import numpy as np
import os
import time
directory = '/Users/danielferreira/Documents/Python_training/wordle'
file = 'sgb-words.csv'
os.chdir(directory)
all = pd.read_csv(file, names=['words'])

def wordle_helper(word_list,method,letter,pos=0):
    if method == 'contains':
        result = word_list[word_list['words'].str.contains(letter)]
    if method == 'not_contains':
        result = word_list[word_list['words'].str.contains(letter)==False]
    if method == 'equal_pos':
        result = word_list[word_list['words'].str[pos-1]==letter]
    if method == 'not_equal_pos':
        result = word_list[word_list['words'].str[pos-1]!=letter]
    
    print(f'First 5 words:\n{result["words"].values[:5]}')
    r = np.random.choice(result['words'])
    print(f'Random Generated:\n{r}')
    
    return result

def byebye():
    print('\nHave a good day!')
    time.sleep(3)
    exit()

menu = 'Press the respective number to filter words that:\n1 - Have a letter\n2 - Do not have a letter\n3 - Have a letter in a position\n4 - Do not have a letter in a position\n5 - Exit\nOption: '
report_break = '-'*70

possible = all.copy()
word = np.random.choice(possible['words'])
print(report_break)
print(f'Hello, here is a word for you: {word}\n')
print(report_break)

mode = 0
while mode!='5':
    print(report_break)
    mode = input(menu)
    if mode == '1':
        print(report_break)
        letter = input('Letter: ')
        print(report_break)
        possible = wordle_helper(possible,'contains',letter)
    elif mode == '2':
        print(report_break)
        letter = input('Letter: ')
        print(report_break)
        possible = wordle_helper(possible,'not_contains',letter)
    elif mode == '3':
        print(report_break)
        position = input('Position: ')
        print(report_break)
        letter = input('Letter: ')
        print(report_break)
        possible = wordle_helper(possible,'equal_pos',letter, pos=int(position))
    elif mode == '4':
        print(report_break)
        position = input('Position: ')
        print(report_break)
        letter = input('Letter: ')
        print(report_break)
        possible = wordle_helper(possible,'not_equal_pos',letter, pos=int(position))
    else:
        byebye()
