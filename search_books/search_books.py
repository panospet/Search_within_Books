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
    """
    Function that returns all data retrieved from the books. Iterates inside
    a given path which contains the list of books, removes digits and
    punctuation and stores the file contents inside a data structure.
    Return type is a dictionary with books names as keys, and as values a
    Counter structure for each word and their occurrence inside each book.
    Example of our structure:
    data_structure = {
        'book1.txt': {
            'word1': 456,
            'word2': 123,
            ...
        }
        'book2.txt': {
            'word3': 256,
            'word4': 100
            ...
        }
        ...
    }
    """
    data_structure = {}
    for file_title in os.listdir(path):
        with open(os.path.join(path, file_title)) as f:
            list_of_words_in_file = remove_numbers_and_punctuation(f.read().lower()).split()
            data_structure[file_title] = Counter(list_of_words_in_file)
    return data_structure


def most_common_words(data, number):
    """
    Function that returns the n most commons words inside all books data.
    It groups all word occurrences from the data given, and returns the
    n most "popular" based on the 'most_common' method of Counter structure.
    Returns a list of tuples containing words and occurrences.
    """
    common_words = Counter()
    for book in data:
        common_words.update(data[book])
    return common_words.most_common(number)


def search_word(data, word):
    """
    Searches for a word inside given books data. If a word appears in a book,
    it's title is stored ahead with the word occurrences. Return value is a
    list of tuples, containing book titles and word occurrences.
    """
    books_occurrence = {}
    for book in data:
        if word in data[book]:
            books_occurrence[book] = data[book][word]
    sorted_books_occurrence = sorted(books_occurrence.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_books_occurrence


if __name__ == "__main__":
    # Just in case we want the program to be run by itself.
    # Calculates the 10 most common words and the occurrences of the word 'auf'.
    # Also logs the total time of every process.
    start_reading_data_time = timeit.default_timer()
    data = store_data('../books')
    stop_reading_data_time = timeit.default_timer()
    store_data_total_time = stop_reading_data_time - start_reading_data_time

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
    print "Reading and storing data total time: " + str(store_data_total_time) + " seconds."
    print "First process took " + str(process1_time) + " seconds."
    print "Second process took " + str(process2_time) + " seconds."
    print "Total time spent: " + str(process1_time + process2_time)
