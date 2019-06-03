# -*- coding: utf-8 -*-

import logging

from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("dcard_seg.txt")
#    model = word2vec.Word2Vec(sentences, size=250)
    model = word2vec.Word2Vec(sentences, workers=20, sg=1, size=300, min_count=50)

    #保存模型，供日後使用
    model.save("word2vec_dcard.model")
#    model.wv.save_word2vec_format('300Tvectors.txt', binary=False)

    #模型讀取方式
    # model = word2vec.Word2Vec.load("your_model_name")

if __name__ == "__main__":
    main()
