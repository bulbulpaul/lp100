# coding: utf-8
import re

def count_char_by_word(word):
    return [ len(sublist) for sublist in re.split(r'\s|"|,|\.', word) if sublist]

def test_count_char_by_word():
    word = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    assert count_char_by_word(word) == pi

if __name__ == '__main__':
    word = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    print(count_char_by_word(word))