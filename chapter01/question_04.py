# coding: utf-8
import re

def extract_chemical_symbols(word, target):
    words = [sublist for sublist in re.split(r'\s|"|,|\.', word) if sublist]
    chemicals = {}
    for index, word in enumerate(words, start=1):
        i = 1 if index in target else 2
        chemicals[word[:i]] = index
    return chemicals

def test_extract_chemical_symbols():
    word = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    target = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    chemicals = {'H':1, 'He':2, 'Li':3, 'Be':4, 'B':5, 'C':6, 'N':7, 'O':8, 'F':9, 'Ne':10, 'Na':11, 'Mi':12, 'Al':13, 'Si':14, 'P':15, 'S':16, 'Cl':17, 'Ar':18, 'K':19, 'Ca':20}
    assert extract_chemical_symbols(word, target) == chemicals

if __name__ == '__main__':
    word = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    target = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    print(extract_chemical_symbols(word, target))