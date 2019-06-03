# -*- coding: utf-8 -*-

import jieba
import json
import logging

import re

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

def contain_zh(word):
#    word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)

    return match


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# jieba custom setting.
jieba.set_dictionary('jieba_dict/dict.txt.big')
jieba.load_userdict("jieba_dict/my.dict.txt")

# load stopwords set
stopword_set = set()
with open('jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))
        
board_lists = ['ntu', 'ncku', 'nthu', 'nctu']

for board_name in board_lists:
    logging.info('處理 {} 版文章 ...'.format(board_name))
    
    article_counter = 0
    with open(board_name+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
        with open(board_name+'_seg.txt', 'w', encoding='utf-8') as output:
            for d in data:
                try:
                    title = d['title']
                except:
                    continue
                content = d['content']
                comments = ''
                for comm in d['comments']:
                    try:
                        comments += ' ' + comm['content']
                    except:
                        pass
                line = (title+content+comments).replace('\n', ' ').strip('\n')
                words = jieba.cut(line, cut_all=False)
                
                for word in words:
                    if word not in stopword_set and contain_zh(word):
                        output.write(word + ' ')
                output.write('\n')
                
                article_counter += 1
    
#                if article_counter % 100 == 0:
#                    logging.info("{}: 已完成 {} 篇文章的斷詞".format(board_name, article_counter))
        
        logging.info("一共 {} 篇文章!".format(article_counter))
