# -*- coding: utf-8 -*-

import operator
import os
import string
import timeit
from collections import Counter
from pprint import pprint


def list_all_files(path):
    files = os.listdir(path)
    return files


def remove_numbers_and_punctuation(str):
    """
    Function that returns input string without any numeric or punctuation characters.
    First of all, we need to remove all 'non-ASCII' characters, because the program considers
    them as words. Then, we remove punctuation and digits.
    The second step is implemented with the 'translate' method, which seems to be more efficient and
    fast, according to this link:
    http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    """
    clean_str = str.decode('unicode_escape').encode('ascii', 'ignore')
    digits_and_punc = string.digits + string.punctuation
    no_num = clean_str.translate(string.maketrans(digits_and_punc, len(digits_and_punc) * " "))
    return no_num


def most_common_words(path, number):
    word_occurrence = {}
    for file_title in list_all_files(path):
        with open(os.path.join(path, file_title)) as f:
            for line in f:
                for word in remove_numbers_and_punctuation(line).lower().split():
                    if word in word_occurrence:
                        word_occurrence[word] += 1
                    else:
                        word_occurrence[word] = 1
    return Counter(word_occurrence).most_common(number)


def search_word_in_books(path, word):
    books_occurrence = {}
    for file_title in list_all_files(path):
        with open(os.path.join(path, file_title)) as f:
            for line in f:
                for w in remove_numbers_and_punctuation(line).lower().split():
                    if w == word:
                        if file_title in books_occurrence:
                            books_occurrence[file_title] += 1
                        else:
                            books_occurrence[file_title] = 1
    sorted_books_occurrence = sorted(books_occurrence.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_books_occurrence


if __name__ == "__main__":
    most_popular = 100
    start1 = timeit.default_timer()
    common_words = most_common_words('../books/', most_popular)
    stop1 = timeit.default_timer()
    process1_time = stop1 - start1

    test_word = 'auf'
    start2 = timeit.default_timer()
    books_and_occurrence = search_word_in_books('../books/', test_word)
    stop2 = timeit.default_timer()
    process2_time = stop2 - start2

    print "The most common words are: "
    pprint(common_words)
    print
    print "Books and occurrences of the word 'auf' "
    pprint(books_and_occurrence)
    print
    print "First process took " + str(process1_time) + " seconds."
    print "Second process took " + str(process2_time) + " seconds."
    print "Total time spent: " + str(process1_time + process2_time)