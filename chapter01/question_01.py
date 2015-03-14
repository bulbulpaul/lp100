# coding: utf-8

def extract_odd_str(x):
    return x[::2]

def test_extract_odd_str():
    assert extract_odd_str('パタトクカシーー') == 'パトカー'
    
if __name__ == '__main__':
    print(extract_odd_str('パタトクカシーー'))