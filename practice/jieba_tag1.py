# -*- coding: utf-8 -*-

import logging
import codecs
import jieba.analyse

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

f = codecs.open('./assets/articles_0.txt', 'r', encoding='utf-8')
count = 0

jieba.set_dictionary('../res/extra_dict/dict.txt.big')
jieba.analyse.set_stop_words('../res/stop_words.txt')
jieba.analyse.set_idf_path('../res/extra_dict/idf.txt.big')
for line in f:
    count += 1
    if count > 20:
        exit()
    tags = jieba.analyse.extract_tags(line.strip(), topK=10)
    print ','.join(tags)
