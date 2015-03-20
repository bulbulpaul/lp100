# coding: utf-8

import random

def typoglycemia(sentence):
    words =  [ shuffle(word) if len(word) > 4 else word for word in sentence.split()]
    return ' '.join(words)

def shuffle(word):
    targets = sorted(word[1:-1], key=lambda k: random.random())
    result = word[0] + ''.join(targets) + word[-1]
    return result

def test_typoglycemia():
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    result = typoglycemia(sentence)
    for src, dest in zip(sentence.split(), result.split()):
        if len(src) > 4:
            assert src[0] == dest[0]
            assert src[-1] == dest[-1]
        else:
            assert src == dest

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(sentence)
    print(typoglycemia(sentence))
    