from collections import Counter

def read_first_column():
    with open('../resource/hightemp.txt') as f:
        c1 = [line.split('\t')[0]for line in f]
    return c1


if __name__ == '__main__':
    columns = read_first_column()
    counter = Counter(columns)
    print(counter.most_common())  