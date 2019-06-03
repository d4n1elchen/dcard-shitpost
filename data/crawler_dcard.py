# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:42:43 2018

@author: daniel
"""

from dcard import Dcard
from dateutil.parser import parse
from dateutil.tz import tzutc
from datetime import datetime
import json

def after_date(after):
    return lambda metas: [m for m in metas if parse(m['createdAt'][:-1]) >= parse(after)]

board_lists = ['ntu', 'ncku', 'nthu', 'nctu']

dcard = Dcard()

for board_name in board_lists:
    print('Crawling '+board_name+' ...')
    
    n = 1300 if board_name == 'ncku' else 300
    
    metas = dcard.forums(board_name).get_metas(num=n, sort='new', callback=after_date('2018-8-1'))
    print('Totally {} posts ...'.format(len(metas)))
    print('Oldest post date: {}'.format(metas[-1]['createdAt']))
    print()
    
    posts = dcard.posts(metas).get()
    
    with open(board_name+'.json', 'w', encoding='utf-8') as f:
        json.dump(posts.result(), f, ensure_ascii=False)