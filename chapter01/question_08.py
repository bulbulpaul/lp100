# coding: utf-8


def cipher(x):
    chars = [chr(219-ord(char)) if char.islower() else char for char in list(x)]
    return ''.join(chars)

def test_template_string():
    word = 'test!テスト&Test'
    ciphe_text = cipher(word)

    # encryption
    assert ciphe_text == 'gvhg!テスト&Tvhg'
    # decryption
    assert cipher(ciphe_text) == word

if __name__ == '__main__':
    word = 'test!テスト&Test'
    print(cipher(word))