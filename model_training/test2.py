# import modules & set up logging
import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1)


# class MySentences(object):
#     def __init__(self, dirname):
#         self.dirname = dirname
#
#     def __iter__(self):
#         for fname in os.listdir(self.dirname):
#             for line in open(os.path.join(self.dirname, fname)):
#                 yield line.split()
#
#
# sentences = MySentences('/some/directory')  # a memory-friendly iterator
# model = gensim.models.Word2Vec(sentences)
#
# model = gensim.models.Word2Vec(iter=1)  # an empty model, no training yet
# model.build_vocab(some_sentences)  # can be a non-repeatable, 1-pass generator
# model.train(other_sentences)  # can be a non-repeatable, 1-pass generator