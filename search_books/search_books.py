# -*- coding: utf-8 -*-

import os
import string
from collections import Counter

BOOKS_PATH = '../books/'


def list_all_files(path):
    files = os.listdir(path)
    return files


def split_file_to_words(path, file_title):
    words = []
    with open(os.path.join(path, file_title)) as f:
        for line in f:
            for word in remove_numbers_and_punctuation(line).split():
                words.append(word)
    return words


def remove_numbers_and_punctuation(str):
    """
    Function that returns input string without any numeric or punctuation characters.
    It is implemented with the 'translate' method, which seems to be more efficient and
    fast, according to this link:
    http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    """
    # stripped = (c for c in str if 0 < ord(c) < 127)
    # str = ''.join(stripped)
    str = str.decode('unicode_escape').encode('ascii', 'ignore')

    digits_and_punc = string.digits + string.punctuation
    no_num = str.translate(string.maketrans(digits_and_punc, len(digits_and_punc) * " "))
    return no_num


def most_common_words(books_path, number):
    words_list = []
    for f in list_all_files(books_path):
        words_list.extend(split_file_to_words(books_path, f))
    return Counter(words_list).most_common(number)


def search_word_in_books(books_path, word):
    books = []
    for f in list_all_files(books_path):
        words_list = split_file_to_words(books_path, f)
        if word in words_list:
            books.append((f, words_list.count(word)))
    books.sort(key=lambda tup: tup[1])
    books.reverse()
    return books


if __name__ == "__main__":
    # print search_word_in_books('../books/', 'bedeutet')

    word_and_occurrences = search_word_in_books('../books/', 'auf')
    # word_and_occurrences.reverse()
    print word_and_occurrences

