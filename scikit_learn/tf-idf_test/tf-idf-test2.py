# -*- coding: utf-8 -*-
import codecs
import os
import jieba
import jieba.posseg as pseg
import sys
import string
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


# 对文档进行分词处理
def seg_words(s, c):
    # 保存分词结果的目录
    sFilePath = './segfile'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)

    # 对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(s, cut_all=True)

    # 对空格，换行符进行处理
    result = []
    for seg in seg_list:
        seg = ''.join(seg.split())
        if seg != '' and seg != "\n" and seg != "\n\n" and seg != "nbsp":
            result.append(seg)

    # 将分词后的结果用空格隔开，保存至本地。比如"我来到北京清华大学"，分词结果写入为："我 来到 北京 清华大学"
    f = codecs.open('{}/{}-seg.txt'.format(sFilePath, c), "w+", 'utf8')
    f.write(' '.join(result))
    f.close()


# 读取已分词好的文档，进行TF-IDF计算
def tf_idf():
    path = './segfile'
    corpus = []
    for i in range(1, 21):
        fname = '{}/{}-seg.txt'.format(path, i)
        print fname
        f = codecs.open(fname)
        content = f.read()
        f.close()
        corpus.append(content)

        vectorizer = CountVectorizer()
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

        word = vectorizer.get_feature_names()  # 所有文本的关键字
        weight = tfidf.toarray()  # 对应的tfidf矩阵

        s_file_path = './tfidffile'
        if not os.path.exists(s_file_path):
            os.mkdir(s_file_path)

        # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
        for i in range(len(weight)):
            f = codecs.open('{}/{}.txt'.format(s_file_path, i), 'w+', 'utf8')
            for j in range(len(word)):
                f.write(word[j] + "	" + str(weight[i][j]) + "\r\n")
            f.close()


def show_key_words():
    path = './tfidffile'
    for i in range(1, 21):
        fname = '{}/{}.txt'.format(path, i)
        f = codecs.open(fname)
        res = {}
        for line in f:
            arr = line.split("\t")
            res[arr[0]] = arr[1].strip()
        f.close()
        sorted_arr = sorted(res.items(), key=lambda item: item[1], reverse=True)
        res_arr = sorted_arr[:10]
        ps = []
        for k, v in res_arr:
            ps.append(k)
        print ', '.join(ps)


if __name__ == "__main__":
    # f = codecs.open('../../make_dict/assets/articles_0.txt', 'r', encoding='utf-8')
    # count = 0

    # jieba.set_dictionary('../../res/extra_dict/dict.txt.big')
    # for line in f:
    #     count += 1
    #     if count > 20:
    #         exit()
    #     seg_words(line.strip(), count)
    tf_idf()
    show_key_words()
