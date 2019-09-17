#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""anagrams.py: remove anagrams element in list"""
__author__ = "phantom1402"
__email__ = "phupham14021992@gmail.com"


def fun_with_anagrams(char_list):
    result_list = []

    while char_list:
        is_anagrams = True
        last_word_str = char_list.pop()

        for word_str in char_list:
            if len(word_str) == len(last_word_str):
                word_set = set(list(word_str))
                last_word_set = set(list(last_word_str))

                if not word_set - last_word_set:  # check is anagrams?
                    is_anagrams = False

        if is_anagrams:
            result_list.append(last_word_str)

    return result_list


if __name__ == '__main__':
    input_list = ['code', 'doce', 'ecod', 'frame', 'framer']
    output_list = fun_with_anagrams(input_list)
    print(output_list)
