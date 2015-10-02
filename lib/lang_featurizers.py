import re
import numpy as np
from collections import Counter
from sklearn.base import TransformerMixin
from textblob import TextBlob


class BagOfWordsFeaturizer(TransformerMixin):
    def __init__(self, num_words=None):
        self.num_words = num_words

    def fit(self, X, y=None):
        words = []
        for x in X:
            x = TextBlob(x.lower())
            words += [word.lemmatize() for word in x.words]
        if self.num_words:
            words = Counter(words)
            self._vocab = [word
                           for word, _ in words.most_common(self.num_words)]
        else:
            self._vocab = list(set(words))
        return self

    def transform(self, X):
        vectors = []
        for x in X:
            x = TextBlob(x.lower())
            word_count = Counter(x.words)
            vector = [0] * len(self._vocab)
            for word, count in word_count.items():
                try:
                    idx = self._vocab.index(word)
                    vector[idx] = count
                except ValueError:
                    pass
            vectors.append(vector)
        return vectors


class FunctionFeaturizer(TransformerMixin):
    def __init__(self, *featurizers):
        self.featurizers = featurizers

    def fit(self, X, y=None):
        '''All SciKit-Learn–Compatible transformers and classifiers
           have the same interface'''
        return self

    def transform(self, X):
        feature_vectors = []
        for x in X:
            feature_vector = [f(x) for f in self.featurizers]
            feature_vectors.append(feature_vector)

        return np.array(feature_vectors)


def percentage_of_punctuation(text):
    total_length = len(text)
    text = re.sub(r'[\w\s]', '', text)
    punct_length = len(text)

    return punct_length / total_length


# Differentiating types of null values

def num_nil(text):
    result = re.findall(r'\W+nil\W+', text)
    if result:
        return len(result)
    else:
        return 0


def num_nil_caps(text):
    result = re.findall(r'\W+NIL\W+', text)
    if result:
        return len(result)
    else:
        return 0


def num_null(text):
    result = re.findall(r'\W+null\W+', text)
    if result:
        return len(result)
    else:
        return 0


def num_none(text):
    result = re.findall(r'\W+None\W+', text)
    if result:
        return len(result)
    else:
        return 0


# Differentiating types of code comments

def num_start_double_semicolons(text):
    result = re.findall(r'^;;', text)
    if result:
        return len(result)
    else:
        return 0


def num_start_hashes(text):
    result = re.findall(r'^#', text)
    if result:
        return len(result)
    else:
        return 0


# Specific to Clojure?
def num_bar_hash(text):
    result = re.findall(r'(^\|\#) | (\#\|$)', text)
    if result:
        return len(result)
    else:
        return 0


# Specific to ?
def num_start_and_end_parenthesis(text):
    result = re.findall(r'\(.*\)$', text)
    if result:
        return len(result)
    else:
        return 0














#
