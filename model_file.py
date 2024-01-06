# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 15:23:51 2023

@author: Aditya
"""

from setup_path import model_name
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(model_name)


# embedding vector
def embed_vec(text1, text2):
    sentences = [text1, text2]
    embeddings = model.encode(sentences)
    return embeddings


# find similarity score using cosine    
def cosine_sim(embeddings):
    sim_score = cosine_similarity([embeddings[0]],[embeddings[1]])
    return sim_score