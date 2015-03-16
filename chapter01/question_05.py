# coding: utf-8

import re

class Ngram():

    def __init__(self, N=3):
        self.N = N

    def char_ngram(self, word):
        c_list = [char for char in list(word) if not char.isspace()]
        return self._ngrams(c_list)

    def word_ngram(self, word):
        w_list = [sublist for sublist in re.split(r'\s|"|,|\.', word) if sublist]
        return self._ngrams(w_list)

    def _ngrams(self, input_list):
        return zip(*[input_list[i:] for i in range(self.N)])

class TestNgram():

    def pytest_funcarg__ngram(request):
        return Ngram(2)

    def test_char_ngram(self, ngram):
        word = 'I am an NLPer'
        c_ngram = [('I', 'a'), ('a', 'm'), ('m', 'a'),('a', 'n'), 
                    ('n', 'N'), ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')]
        chars = ngram.char_ngram(word)
        assert list(chars) == c_ngram

    def test_word_ngram(self, ngram):
        word = 'I am an NLPer'
        w_ngram = [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]
        words = ngram.word_ngram(word)
        assert list(words) == w_ngram

if __name__ == '__main__':
    word = 'I am an NLPer'
    ngram = Ngram(2)
    # word bi-gram
    words = ngram.word_ngram(word)
    for w in words:
        print(w)

    # char bi-gram
    chars = ngram.char_ngram(word)
    for c in chars:
        print(c)