# encoding=utf-8
import os
import codecs
import json
import re

import jieba

# jieba.enable_parallel()

stop_words = [
    u'the',
    u'of',
    u'is',
    u'and',
    u'to',
    u'in',
    u'that',
    u'we',
    u'for',
    u'an',
    u'are',
    u'by',
    u'be',
    u'as',
    u'on',
    u'with',
    u'can',
    u'if',
    u'from',
    u'which',
    u'you',
    u'it',
    u'this',
    u'then',
    u'at',
    u'have',
    u'all',
    u'not',
    u'one',
    u'has',
    u'or',
    u'that',
    u'的',
    u'了',
    u'和',
    u'是',
    u'就',
    u'都',
    u'而',
    u'及',
    u'與',
    u'著',
    u'或',
    u'一個',
    u'沒有',
    u'我們',
    u'你們',
    u'妳們',
    u'他們',
    u'她們',
    u'是否',
    u'是否',
]

f = codecs.open('./assets/articles_0.txt', 'r', encoding='utf-8')
count = 0

words = {}


def print_result():
    sw = sorted(words.items(), key=lambda d: d[1])
    for (k, v) in sw:
        print u'{0} : {1}'.format(k, v)


for line in f:
    count += 1
    if count > 10:
        print_result()
        exit()
    line = line.strip('/r/n')
    content = re.sub(ur'[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：「」；]+', u'', line)
    for w in jieba.cut(content):
        if w in stop_words:
            continue
        if w in words:
            words[w] += 1
        else:
            words[w] = 1
