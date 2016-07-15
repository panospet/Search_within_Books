# -*- coding: utf-8 -*-

import operator
import os
import string
import timeit
from collections import Counter
from pprint import pprint


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


def store_data(path):
    data_structure = {}
    for file_title in os.listdir(path):
        with open(os.path.join(path, file_title)) as f:
            file_list = remove_numbers_and_punctuation(f.read().lower()).split()
            data_structure[file_title] = Counter(file_list)
    return data_structure


def most_common_words(data, number):
    common_words = Counter()
    for book in data:
        common_words.update(data[book])
    return common_words.most_common(number)


def search_word(data, word):
    books_occurrence = {}
    for book in data:
        if word in data[book]:
            books_occurrence[book] = data[book][word]
    sorted_books_occurrence = sorted(books_occurrence.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_books_occurrence


if __name__ == "__main__":
    data = store_data('../books')

    most_popular = 10
    start1 = timeit.default_timer()
    common = most_common_words(data, most_popular)
    stop1 = timeit.default_timer()
    process1_time = stop1 - start1

    test_word = 'auf'
    start2 = timeit.default_timer()
    books_and_occurrence = search_word(data, test_word)
    stop2 = timeit.default_timer()
    process2_time = stop2 - start2

    print "The most common words are: "
    pprint(common)
    print
    print "Books and occurrences of the word " + test_word + ":"
    pprint(books_and_occurrence[:10])
    print
    print "First process took " + str(process1_time) + " seconds."
    print "Second process took " + str(process2_time) + " seconds."
    print "Total time spent: " + str(process1_time + process2_time)
