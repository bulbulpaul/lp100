# coding: utf-8

def alternately_merge(x ,y):
    return ''.join([item for sublist in zip(x,y) for item in sublist])

def test_alternately_merge():
    assert alternately_merge('パトカー', 'タクシー') == 'パタトクカシーー'
    
if __name__ == '__main__':
    print(alternately_merge('パトカー', 'タクシー'))