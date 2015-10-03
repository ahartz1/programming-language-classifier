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
# Ruby
def presence_nil(text):
    result = re.findall(r'\W+nil\W+', text)
    if result:
        return 1
    return 0


def presence_nil_caps(text):
    result = re.findall(r'\W+NIL\W+', text)
    if result:
        return 1
    return 0


def presence_null(text):
    result = re.findall(r'\W+null\W+', text)
    if result:
        return 1
    return 0


def presence_none(text):
    result = re.findall(r'\W+None\W+', text)
    if result:
        return 1
    return 0


# Differentiating types of code comments
# Scheme
def presence_start_double_semicolons(text):
    result = re.findall(r'(^;;) | (\n;;)', text)
    if result:
        return 1
    return 0


def presence_start_hashes(text):
    result = re.findall(r'(^#) | (\n#)', text)
    if result:
        return 1
    return 0



def presence_bar_hash(text):
    result = re.findall(r'(\n\|\#) | (\#\|\n)', text)
    if result:
        return 1
    return 0


# Specific to Scheme
def percent_start_and_end_parenthesis(text):
    total_length = re.findall(r'($|\n)', text)
    result = re.findall(r'\s*\(.*\)\s*\n', text)
    if result:
        return len(result) / len(total_length)
    return 0


# Specific to C#
def presence_void(text):
    result = re.findall(r'\s+void\s+', text)
    if result:
        return 1
    return 0


def presence_public(text):
    result = re.findall(r'\s+public\s+', text)
    if result:
        return 1
    return 0


def presence_bool(text):
    result = re.findall(r'\s+bool\s+', text)
    if result:
        return 1
    return 0

# NOT USED DUE TO LOWERED SCORES!
def presence_int(text):
    result = re.findall(r'\s+int\s+', text)
    if result:
        return 1
    return 0


# Specific to Ruby
def presence_module_line(text):
    result = re.findall(r'(?:^|\n)\s*module ([A-Z][a-z]*)+', text)
    if result:
        return 1
    return 0


def presence_extend_line(text):
    result = re.findall(r'(?:^|\n)\s*extend ([A-Z][a-z]*)+::([A-Z][a-z]*)+',
                        text)
    if result:
        return 1
    return 0


def presence_require_line(text):
    result = re.findall(r'(?:^|\n)\s*require .+', text)
    if result:
        return 1
    return 0


def presence_end(text):
    result = re.findall(r'(?:^|\n)\s*end\s*(?:$|\n)', text)
    if result:
        return 1
    return 0


def presence_multiple_end(text):
    result = re.findall(r'(\n\s*end\s*(?:$|\n)){2,}', text)
    if result:
        return 1
    return 0


def presence_def_no_colon(text):
    result = re.findall(r'((?:^|\n)\s*def[^:]*(?:$|\n)){1}', text)
    if result:
        return 1
    return 0


def presence_at(text):
    result = re.findall(r'@[\w]+', text)
    if result:
        return 1
    return 0


def presence_double_at(text):
    result = re.findall(r'@@[\w]+', text)
    if result:
        return 1
    return 0


# Specific to Clojure
def presence_defn(text):
    result = re.findall(r'(?:^|\n)\s*\(\s*defn', text)
    if result:
        return 1
    return 0


def percent_consecutive_closing_paren(text):
    total_length = re.findall(r'($|\n)', text)
    result = re.findall(r'\){2,}(?:$|\n)', text)
    if result:
        return len(result) / len(total_length)
    return 0


# Specific to Python
def presence_from_import_line(text):
    result = re.findall(r'(?:^|\n)\s*from\s+[a-z_\.]+\s+import\s+[\w\.*]+',
                        text)
    if result:
        return 1
    return 0


def presence_import_line(text):
    result = re.findall(r'(?:^|\n)\s*import\s+[a-z_\.*]+', text)
    if result:
        return 1
    return 0


def presence_print(text):
    result = re.findall(r'\n\s*print\(', text)
    if result:
        return 1
    return 0


def presence_dot_join(text):
    result = re.findall(r'\.join\(', text)
    if result:
        return 1
    return 0


def presence_dot_format(text):
    result = re.findall(r'(\'|")\.format\(', text)
    if result:
        return 1
    return 0


def presence_dot_values(text):
    result = re.findall(r'\.values\(\)', text)
    if result:
        return 1
    return 0


def presence_dunder_name(text):
    result = re.findall(r'\nif __name__ == \'__main__\':\n', text)
    if result:
        return 1
    return 0


def presence_dunder_init(text):
    result = re.findall(r'(?:^|\n)\s*def __init__\(self.*\):\n', text)
    if result:
        return 1
    return 0


def presence_def_colon(text):
    result = re.findall(r'^|\ndef .*:\n', text)
    if result:
        return 1
    return 0







#
