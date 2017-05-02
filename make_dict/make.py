# encoding=utf-8
import os
import codecs
import json
import re

import jieba

# jieba.enable_parallel()

stop_words = []
sf = codecs.open('../res/stop_words.txt', 'r', encoding='utf-8')
for line in sf:
    stop_words.append(line.strip())

f = codecs.open('./assets/articles_0.txt', 'r', encoding='utf-8')
count = 0

words = {}


def print_result():
    sw = sorted(words.items(), key=lambda d: d[1])
    for (k, v) in sw:
        print u'{0} : {1}'.format(k, v)


for line in f:
    count += 1
    print count
    if count > 50:
        print_result()
        exit()
    line = line.strip()
    content = re.sub(ur'[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：「」；]+', u'', line)
    for w in jieba.cut(content,cut_all=True):
        if w in stop_words:
            continue
        if w in words:
            words[w] += 1
        else:
            words[w] = 1
