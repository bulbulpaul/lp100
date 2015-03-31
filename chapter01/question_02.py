# coding: utf-8

def alternately_merge(x ,y):
    return ''.join([sub_x + sub_y for sub_x, sub_y in zip(x,y)])

def easy_alternately_merge(x ,y):
    return ''.join(sum(zip(x, y), ()))

def test_alternately_merge():
    assert alternately_merge('パトカー', 'タクシー') == 'パタトクカシーー'
    
if __name__ == '__main__':
    print(easy_alternately_merge('パトカー', 'タクシー'))