# coding: utf-8

class Ngram():

    def __init__(self, N=3):
        self.N = N

    def char_ngram(self, word):
        c_list = [char for char in list(word) if not char.isspace()]
        return self._ngrams(c_list)

    def _ngrams_tuple(self, input_list):
        return zip(*[input_list[i:] for i in range(self.N)])

    def _ngrams(self, input_list):
        return [input_list[index-1] + input_list[index] for index in range(1, len(input_list))]

    def union_set(self, x ,y):
        return (set(x) | set(y))

    def product_set(self, x, y):
        return (set(x) & set(y))

    def difference_set(self, x, y):
        return (set(x) ^ set(y))

class TestNgram():

    def pytest_funcarg__ngram(request):
        return Ngram(2)

    def test_char_ngram(self, ngram):
        x = 'paraparaparadise'
        y = 'paragraph'

        # char bi-gram
        x_bigram = ngram.char_ngram(x)
        y_bigram = ngram.char_ngram(y)

        union = set(['gr', 'ad', 'ap', 'ph', 'pa', 'is', 'ar', 'ag', 'se', 'ra', 'di'])
        product = set(['ra', 'ar', 'ap', 'pa'])
        defference = set(['gr', 'ag', 'ad', 'is', 'se', 'ph', 'di'])

        assert ngram.union_set(x_bigram, y_bigram) == union
        assert ngram.product_set(x_bigram, y_bigram) == product
        assert ngram.difference_set(x_bigram, y_bigram) == defference

if __name__ == '__main__':
    x = 'paraparaparadise'
    y = 'paragraph'
    ngram = Ngram(2)

    # char bi-gram
    x_bigram = ngram.char_ngram(x)
    y_bigram = ngram.char_ngram(y)

    # Union set
    print('union set: ' + str(ngram.union_set(x_bigram, y_bigram)))

    # Product set
    print('product set: ' + str(ngram.product_set(x_bigram, y_bigram)))

    # Defference set
    print('difference set: ' + str(ngram.difference_set(x_bigram, y_bigram)))

    # contains 'se'
    print('contains "se":' + str('se' in x_bigram and 'se' in y_bigram))