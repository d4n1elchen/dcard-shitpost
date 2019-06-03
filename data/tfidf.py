# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 08:17:38 2018

@author: daniel
"""

import numpy as np
import pandas as pd
from collections import defaultdict, OrderedDict
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import re

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

def contain_zh(word):
#    word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)

    return match

#%% Word count
word_counts = []
total_cnt = defaultdict(int)
with open('ncku_seg.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()
        cnt = defaultdict(int)
        for word in words:
            if not contain_zh(word):
                continue
            cnt[word] += 1
            total_cnt[word] += 1
        word_counts.append(cnt)

#%% Training  
vectorizer = DictVectorizer()
tfidf = TfidfTransformer()

print('Vectorize')
vec = vectorizer.fit_transform(word_counts)
feature_names = np.array(vectorizer.get_feature_names())

print('Calculating TFIDF')
tfidfs = tfidf.fit_transform(vec)

#%% Insight
top_20_words = []
for t in tfidfs:
    t = t.toarray().flatten()
    sorted_tfidf_idx = np.argsort(t)[::-1]
    top_20_words.append(feature_names[sorted_tfidf_idx[:20]])

#%% overall tfidf
t_vec = vectorizer.transform(total_cnt)
t_tfidf = tfidf.transform(t_vec)
t_tfidf = t_tfidf.toarray().flatten()
sorted_tfidf_idx = np.argsort(t_tfidf)[::-1]
top_20_words_overall = feature_names[sorted_tfidf_idx[:20]].tolist()

#%% word count
sorted_cnt = sorted(total_cnt.items(), key=lambda k: k[1], reverse=True)
top_30_freq_words = [s[0] for s in sorted_cnt[:30]]
pd.DataFrame(sorted_cnt).to_csv('ncku_cnt.csv')