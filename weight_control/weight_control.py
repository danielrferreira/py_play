#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:56:38 2023

@author: danielferreira
"""


# Setup

import pandas as pd
import time
from datetime import date
import matplotlib.pyplot as plt
import os

directory = '/Users/danielferreira/Documents/Python_training/weight'
file = 'weight.csv'

os.chdir(directory)

# Functions
def week_report(w,e,f):
    w_kg = round(w * 0.45359237,1)
    if e<=1:
        message1='You need to exercise.'
    elif e<=2:
        message1='You can exercise more.'
    else:
        message1='Good Job.'
    if f<=3:
        message2='You need to eat better.'
    elif f<=7:
        message2='You can eat better.'
    else:
        message2='Keep up the good job eating well'
    print(f'\nYour weight week average is {w} lbs ({w_kg} kgs)')
    print(f'\nYou exercised {e} times.',message1)
    print(f'\nYour week nutrition level is {f}.',message2)

def byebye():
    print('\nHave a good day!')
    time.sleep(3)
    exit()

def daily_report(w,e,f):
    w_kg = round(w * 0.45359237,1)
    print(f'\nWeight = {w} lbs ({w_kg} kgs).')
    if e>=1:
        print('\nYou did exercise. Good Job!')
    else:
        print('\nYou did not exercise.')
    print(f'\nYour daily nutrition level is {f}.')
    
def time_graph(data):
    data.set_index('date', inplace=True)
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['weight_lbs'], label='Value', color='blue')
    plt.title('weight over time')
    plt.xlabel('Date')
    plt.ylabel('Weight in lbs')
    plt.grid(True)
    plt.legend()
    plt.savefig('last_graph.png')
    os.system('open last_graph.png')


# Welcome
print('\nGood Morning, Daniel! I hope you had a restful night.')

# Import Data
weight_df = pd.read_csv(file)
w1 = round(weight_df['weight_lbs'][-7:].mean(),1)
e1 = weight_df['exer'][-7:].sum()
f1 = round(weight_df['food'][-7:].mean(),1)

# Week Report
print('\nLets have a look on your current week.')
week_report(w1,e1,f1)
time_graph(weight_df)

# Data Input
status = input('\nDo you want to add data? If yes, press y: ')
if status == 'y':
    w2 = float(input('\nPlease enter your weigth: '))
    e2 = int(input('\nDid you exercise? '))
    f2 = int(input('\nHow well did you eat yesterday? '))
else:
    byebye()

# Confirm Results
print('\nLets see your Inputs:')
daily_report(w2,e2,f2)
status = input('\nIs that correct? Press y to confirm: ')
if status != 'y':
    byebye()

# New week data
today = date.today().strftime('%Y-%m-%d')
new_row = pd.DataFrame([{'date':today,'weight_lbs':w2,'exer':e2,'food':f2}])
new_data = pd.concat([weight_df,new_row])
w3 = round(new_data['weight_lbs'][-7:].mean(),1)
e3 = new_data['exer'][-7:].sum()
f3 = round(new_data['food'][-7:].mean(),1)

# Week Report (Updated)
print('\nOk. Lets have a look on your current week with the new data:.')
week_report(w3,e3,f3)

# Save and Exit
status = input('\nDo you want to save and exit? If yes, press y: ')
if status == 'y':
    new_row.to_csv(file, header=False,index=False, mode='a')
    print('\nDone!!!!')
    weight_df = pd.read_csv(file)
    time_graph(weight_df)
    byebye()
else:
    byebye()
