# -*- coding: utf-8 -*-

import sys  
import os
from TextPreprocess import TextPreprocess  # 第一个是文件名，第二个是类名

# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')
# 实例化这个类
tp = TextPreprocess()
tp.corpus_path = "./text_corpus2_small/"    #原始语料路径
tp.pos_path = "text_corpus2_pos/"       #预处理后语料路径
tp.segment_path = "text_corpus2_segment/"   #分词后语料路径
tp.wordbag_path = "./text_corpus2_wordbag/"   #词袋模型路径
tp.stopword_path = "./extra_dict/hlt_stop_words.txt"  #停止词路径
tp.trainset_name = "trainset.dat"      #训练集文件名
tp.wordbag_name = "wordbag.dat"       #词包文件名
# tp.preprocess()
# tp.segment()
# tp.train_bag()
tp.tfidf_bag()

# tp.verify_trainset()
# tp.verify_wordbag()