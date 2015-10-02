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


# Differentiating types of null values

def percent_nil(text):
    total_length = len(text)
    result = re.findall(r'\W+nil\W+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


def percent_nil_caps(text):
    total_length = len(text)
    result = re.findall(r'\W+NIL\W+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


def percent_null(text):
    total_length = len(text)
    result = re.findall(r'\W+null\W+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


def percent_none(text):
    total_length = len(text)
    result = re.findall(r'\W+None\W+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


# Differentiating types of code comments
# Scheme
def percent_start_double_semicolons(text):
    total_length = len(text)
    result = re.findall(r'^;;', text)
    if result:
        return len(result) / total_length
    else:
        return 0


def percent_start_hashes(text):
    total_length = len(text)
    result = re.findall(r'^#', text)
    if result:
        return len(result) / total_length
    else:
        return 0


# Specific to Clojure?
def percent_bar_hash(text):
    total_length = len(text)
    result = re.findall(r'(^\|\#) | (\#\|$)', text)
    if result:
        return len(result) / total_length
    else:
        return 0


# Specific to Scheme TODO: Make percent of total LINES, not words
def percent_start_and_end_parenthesis(text):
    total_length = re.findall(r'\n', text)
    result = re.findall(r'\(.*\)$', text)
    if result:
        return len(result) / len(total_length)
    else:
        return 0


# Specific to C#
def percent_void(text):
    total_length = len(text)
    result = re.findall(r'\s+void\s+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


def percent_public(text):
    total_length = len(text)
    result = re.findall(r'\s+public\s+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


def percent_bool(text):
    total_length = len(text)
    result = re.findall(r'\s+bool\s+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


def percent_int(text):
    total_length = len(text)
    result = re.findall(r'\s+int\s+', text)
    if result:
        return len(result) / total_length
    else:
        return 0


# Specific to Ruby
def presence_module_line(text):
    result = re.findall(r'module ([A-Z][a-z]*)+', text)
    if result:
        return 1
    else:
        return 0


def presence_extend_line(text):
    result = re.findall(r'extend ([A-Z][a-z]*)+::([A-Z][a-z]*)+', text)
    if result:
        return 1
    else:
        return 0


def presence_require_line(text):
    result = re.findall(r'^\s*require .+', text)
    if result:
        return 1
    else:
        return 0


def presence_end(text):
    result = re.findall(r'^\s*end\s*$', text)
    if result:
        return 1
    else:
        return 0








#
