# coding: utf-8


def cipher(x):
    chars = [chr(216-ord(char)) if char.islower() else char for char in list(x)]
    print(str(chars))
    return ''.join(chars)

def test_template_string():
    word = 'test!テスト&Test'
    assert cipher(word) == 'dsed!テスト&Tsed'

if __name__ == '__main__':
    word = 'test!テスト&Test'
    print(cipher(word))