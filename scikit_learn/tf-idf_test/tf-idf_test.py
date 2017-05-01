# -*- coding: utf-8 -*-

import sys
import os
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入训练集
corpus = ["我 来到 北京 清华大学 了",  # 第一类文本切词后的结果，词之间以空格隔开
          "他 来到 了 网易 杭研 大厦",  # 第二类文本的切词结果
          "小明 硕士 毕业 与 中国 科学院",  # 第三类文本的切词结果
          "我 爱 得 北京 天安门"]  # 第四类文本的切词结果

# 从文件导入停用词表
stpwrdpath = "../extra_dict/hlt_stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()
# 将停用词表转换为list
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()

# 将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer(stop_words=stpwrdlst)  # 创建词袋数据结构
# 创建hash向量词袋
# vectorizer = HashingVectorizer(stop_words =stpwrdlst,n_features = 10000) #设置停用词词表,设置最大维度10000

# 统计每个词语的tf-idf权值
transformer = TfidfTransformer()
# 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
wordlist = vectorizer.get_feature_names()  # 获取词袋模型中的所有词
# tf-idf矩阵 元素a[i][j]表示j词在i类文本中的tf-idf权重
weightlist = tfidf.toarray()
# 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
for i in range(len(weightlist)):
    print "-------这里输出第", i, "类文本的词语tf-idf权重------"
    for j in range(len(wordlist)):
        print wordlist[j], weightlist[i][j]
