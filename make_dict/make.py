# encoding=utf-8
import os
import codecs
import json
import jieba

# jieba.enable_parallel()

f = codecs.open('./assets/articles.json', 'r', encoding='utf-8')
count = 0

for line in f:
    count += 1
    if count > 1:
        exit()
    js = json.loads(line)
    content = js['content']
    # tags = jieba.analyse.extract_tags(content, topK=10)
    # print(",".join(tags))
    words = "/ ".join(jieba.cut(content))
    print words
