# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:11:40 2018

@author: daniel
"""

board_lists = ['ntu', 'ncku', 'nthu', 'nctu']

with open('dcard_seg.txt', 'w', encoding='utf-8') as outfile:
    for board_name in board_lists:
        with open(board_name+'_seg.txt', 'r', encoding='utf-8') as infile:
            outfile.write(infile.read().strip('\n'))