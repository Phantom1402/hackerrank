#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""anagrams.py: remove anagrams element in list"""
__author__ = "phantom1402"
__email__ = "phupham14021992@gmail.com"


def fun_with_anagrams(char_list):
    result_list = []
    tmp_list = []
    sorted_char_iterator = map(lambda x: (x, ''.join(sorted(x))), char_list)

    for char_tup in sorted_char_iterator:
        if char_tup[1] not in tmp_list:
            tmp_list.append(char_tup[1])
            result_list.append(char_tup[0])

    return result_list


if __name__ == '__main__':
    input_list = ['code', 'doce', 'ecod', 'frame', 'framer']
    output_list = fun_with_anagrams(input_list)
    print(output_list)
