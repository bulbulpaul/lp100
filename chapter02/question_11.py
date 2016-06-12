# coding:utf-8
import argparse


def _readfile_with(file_name, fn) :
    """
    read file with execute function 
    :param str fil_name: open file name
    :param function fn: execute function
    :rtype: str
    :return: string after function adaptation
    """
    with open(file_name) as f:
        for line in f:
            yield fn(line) if not fn is None else line

def init_parser():
    """
    argument paser setting
    :return argument parser
    """
    parser = argparse.ArgumentParser(description='Replace tabs to spaces')
    parser.add_argument('file', help='target file')
    return parser

def tab2space(text, tabsize=1):
    """
    replace tab to space character
    :param str text: target string
    :param int tabsize: replace size
    :rtype str
    :return replaced text
    """
    return text.expandtabs(tabsize)

def readfile_with_replace(file_name):
    """
    :param str file_name: target file path
    :return 
    """
    for line in _readfile_with(file_name, tab2space):
        yield line

def test_tab2space():
    parser = init_parser()
    args = parser.parse_args(['../resource/hightemp.txt'])
    assert 'test test' == tab2space('test\ttest')
    

if __name__ == '__main__':
    # argument setting 
    parser = init_parser()
    # argument parse
    args = parser.parse_args()
    if args.file:
        for line in  readfile_with_replace(args.file):
            # since the string contains a line separator
            print(line, end="")
    else :
        print('not support')