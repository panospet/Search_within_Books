from search_books.search_books import *
import unittest


def simple_search_word(word):
    books_occurrence = {}
    for file_title in os.listdir('../books/'):
        with open(os.path.join('../books/', file_title)) as f:
            for line in f:
                for w in remove_numbers_and_punctuation(line).lower().split():
                    if w == word:
                        if file_title in books_occurrence:
                            books_occurrence[file_title] += 1
                        else:
                            books_occurrence[file_title] = 1
    sorted_books_occurrence = sorted(books_occurrence.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_books_occurrence


def simple_common_words(number):
    word_occurrence = {}
    for file_title in os.listdir('../books/'):
        with open(os.path.join('../books/', file_title)) as f:
            for line in f:
                for word in remove_numbers_and_punctuation(line).lower().split():
                    if word in word_occurrence:
                        word_occurrence[word] += 1
                    else:
                        word_occurrence[word] = 1
    res = dict(Counter(word_occurrence).most_common(number))
    sorted_res = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_res


class TestSearchBooks(unittest.TestCase):
    def setUp(self):
        self.data = store_data('../books/')
        self.test_word = 'auf'

    def tearDown(self):
        pass

    def test_common_words_with_simple(self):
        word_occurrence = most_common_words(self.data, 10)
        simple = simple_common_words(10)
        self.assertEqual(word_occurrence, simple)

    # def test_search_word_with_simple(self):
    #     books_and_occurrence = search_word(self.data, self.test_word)
    #     simple = simple_search_word(self.test_word)
    #     self.assertEqual(books_and_occurrence, simple)

    def test_store_data_has_correct_size(self):
        self.assertEqual(len(self.data), 557)

    def test_random_word_search(self):
        books_and_occurrence = search_word(self.data, self.test_word)
        self.assertEqual(books_and_occurrence[:10], [('10223-8.txt', 6052),
                                                     ('10223-0.txt', 6052),
                                                     ('31114-8.txt', 2137),
                                                     ('17383-8.txt', 1756),
                                                     ('12921.txt', 1754),
                                                     ('12921-8.txt', 1754),
                                                     ('17379-8.txt', 1573),
                                                     ('28751-8.txt', 1353),
                                                     ('23333-8.txt', 1304),
                                                     ('23756-8.txt', 1301)])

    def test_most_common_words(self):
        common = most_common_words(self.data, 10)
        self.assertEqual(common, [('und', 883768),
                                  ('die', 779996),
                                  ('der', 752828),
                                  ('in', 462536),
                                  ('zu', 334216),
                                  ('den', 330914),
                                  ('sie', 330585),
                                  ('er', 300633),
                                  ('das', 299255),
                                  ('von', 264353)])


if __name__ == "__main__":
    unittest.main()
