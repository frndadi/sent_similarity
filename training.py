# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:57:05 2023

@author: Aditya
"""

import pandas as pd
from utils import run_common_steps
from setup_path import csv_path, destn_path
from model_file import embed_vec, cosine_sim


def training_steps():

    text_data = pd.read_csv(csv_path)
    
    filtrd_df = run_common_steps(text_data)
    
    text_data['Score']=''
    score_lst = []
    # for ind  in filtrd_df.index:
    #     sent1 = filtrd_df['text1'][ind]
    #     sent2 = filtrd_df['text2'][ind]    
        
    sent1_lst = filtrd_df['text1'].tolist()
    sent2_lst = filtrd_df['text2'].tolist()
    count =0
    for sent1, sent2 in zip(sent1_lst, sent2_lst):
        
        embedings = embed_vec(sent1,sent2)
        score = cosine_sim(embedings)[0]
        score_lst.extend(score)
        text_data['Score'].iloc[count]=score[0]
        
        count+=1
        if count%100==0:
            print("count: ", str(count))
    
    #text_data['Score'] =  score_lst
    text_data.to_csv(destn_path)

