# coding:utf-8
import argparse


def init_parser():
    parser = argparse.ArgumentParser(description='Word count')
    parser.add_argument('-l', '--lines', action = 'store_true', dest = 'lines', help='return the number of rows')
    parser.add_argument('file', help='target file')
    return parser

def line_count(file_name):
    return sum(1 for l in open(file_name))

def test_line_count():
    # argument setting 
    parser = init_parser()
    args = parser.parse_args(['-l', '../resource/hightemp.txt'])
    assert(True, args.lines)
    assert(24, line_count(args.file))

if __name__ == '__main__':

    # argument setting 
    parser = init_parser()
    # parse
    args = parser.parse_args()
    if args.lines:
        # line count
        print(line_count(args.file))
    else :
        print('not support')