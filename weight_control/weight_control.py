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
import numpy as np

directory = '../data'
file = 'weight.csv'
os.chdir(directory)
report_break = '-'*70

# Functions
def week_report(w_current,w_past,e,f):
    w_kg_current = round(w_current * 0.45359237,1)
    w_kg_past = round(w_past * 0.45359237,1)
    diff = w_current-w_past
    diff_kg = w_kg_current-w_kg_past
    diff_pct = diff/w_past
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
    print(report_break)
    print(f'\nYour weight week average is {w_current} lbs ({w_kg_current} kgs)')
    print(f'\nIn the last 7 days, your balance is {diff:.2} lbs ({diff_kg:.2} kgs). Weight loss percentage = {diff_pct:.2%}')
    print(f'\nSince you started to track, you lost {(168.2-w_current):.2} lbs ({((168.2-w_current)*0.45359237):.2} kgs).')
    print(f'\nYou exercised {e} times.',message1)
    print(f'\nYour week nutrition level is {f}.',message2)

def byebye():
    print(report_break)
    print('\nHave a good day!')
    time.sleep(3)
    exit()

def daily_report(w,e,f):
    w_kg = round(w * 0.45359237,1)
    print(report_break)
    print(f'\nWeight = {w} lbs ({w_kg} kgs).')
    if e>=1:
        print('\nYou did exercise. Good Job!')
    else:
        print('\nYou did not exercise.')
    print(f'\nYour daily nutrition level is {f}.')
    
def time_graph(data):
    data.set_index('date', inplace=True)
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['weight_lbs'], label='Daily Weight', color='blue')
    plt.plot(data.index, data['avg_7d'], label='Last 7 d average', color='red', linestyle='--')
    plt.axhline(y=154.324, color='green', linestyle=':', label='Goal')
    plt.title('weight over time')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Weight in lbs')
    plt.grid(True)
    plt.legend()
    plt.savefig('last_graph.png')
    os.system('open last_graph.png')

# Welcome
print(report_break)
print('\nGood Morning, Daniel! I hope you had a restful night.')
print(report_break)

# Import Data
weight_df = pd.read_csv(file)
w1_current = float(round(weight_df['avg_7d'].iloc[-1],1))
w1_past = float(round(weight_df['avg_7d'].iloc[-8],1))
e1 = weight_df['exer'][-7:].sum()
f1 = round(weight_df['food'][-7:].mean(),1)

# Week Report
print('\nLets have a look on your current week.')
week_report(w1_current,w1_past,e1,f1)
time_graph(weight_df)

# Data Input
print(report_break)
status = input('\nDo you want to add data? If yes, press y: ')
if status == 'y':
    w2 = float(input('\nPlease enter your weigth: '))
    e2 = int(input('\nDid you exercise? '))
    f2 = int(input('\nHow well did you eat yesterday? '))
else:
    byebye()

# Confirm Results
print(report_break)
print('\nLets see your Inputs:')
daily_report(w2,e2,f2)
status = input('\nIs that correct? Press y to confirm: ')
if status != 'y':
    byebye()

# New week data
today = date.today().strftime('%Y-%m-%d')
new_avg_list = (list(weight_df['weight_lbs'][-6:]))
new_avg_list.append(w2)
new_avg = round(np.array(new_avg_list).mean(),2)
new_row = pd.DataFrame([{'date':today,'weight_lbs':w2,'exer':e2,'food':f2, 'avg_7d':new_avg}])
new_data = pd.concat([weight_df,new_row])
w3_current = float(round(new_data['avg_7d'].iloc[-1],1))
w3_past = float(round(new_data['avg_7d'].iloc[-8],1))
e3 = new_data['exer'][-7:].sum()
f3 = round(new_data['food'][-7:].mean(),1)

# Week Report (Updated)
print(report_break)
print('\nOk. Lets have a look on your current week with the new data:.')
week_report(w3_current,w3_past,e3,f3)

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