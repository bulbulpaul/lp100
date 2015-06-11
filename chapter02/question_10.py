# coding:utf-8
import argparse


def init_parser():
    parser = argparse.ArgumentParser(description='Word count')
    parser.add_argument('file', help='target file')
    return parser

def line_count(file_name):
    result = 0
    with open(file_name) as f:
        result = sum(1 for l in f)
    return result

def test_line_count():
    # argument setting 
    parser = init_parser()
    args = parser.parse_args(['../resource/hightemp.txt'])
    assert 24 == line_count(args.file)

if __name__ == '__main__':

    # argument setting 
    parser = init_parser()
    # parse
    args = parser.parse_args()
    if args.file:
        # line count
        print(line_count(args.file))
    else :
        print('not support')