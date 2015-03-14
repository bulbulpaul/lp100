# coding: utf-8

def reverse_char(string):
    return string[::-1]

def test_reverse_char():
    assert reverse_char('stressed') == 'desserts'

if __name__ == '__main__':
    print(reverse_char('stressed'))