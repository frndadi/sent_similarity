# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:59:34 2023

@author: Aditya
"""

import re
# import tqdm


def quotes_removal(sent):
    # specific
    sent = re.sub(r"won't", "will not", sent)
    sent = re.sub(r"can\'t", "can not", sent)

    # general
    sent = re.sub(r"n\'t", " not", sent)
    sent = re.sub(r"\'re", " are", sent)
    sent = re.sub(r"\'s", " is", sent)
    sent = re.sub(r"\'d", " would", sent)
    sent = re.sub(r"\'ll", " will", sent)
    sent = re.sub(r"\'t", " not", sent)
    sent = re.sub(r"\'ve", " have", sent)
    sent = re.sub(r"\'m", " am", sent)
    return sent


def run_common_steps(text_data):

    for item in list(text_data):

        preprocessed_text = []
        for sentance in text_data[item].values:
            sent = quotes_removal(sentance)
            sent = sent.replace('\\r', ' ')
            sent = sent.replace('\\"', ' ')
            sent = sent.replace('\\n', ' ')
            sent = sent.replace('\\n', ' ')
           
           # sent = ' '.join(e for e in sent.split() if e not in stopwords.words('english'))
            preprocessed_text.append(sent.lower().strip())

         # Merging preprocessed_text in text_data
        text_data[item] = preprocessed_text
    return text_data