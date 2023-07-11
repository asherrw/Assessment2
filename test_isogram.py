import unittest
from conceptIsogram import is_isogram

class TestingSentences(unittest.TestCase):

    # test to see if unittest module runs properly
    def test_for_example(self):
        a = 4
        b = 3
        c = 1
        self.assertEqual(c == (a-b), True)

    # test to see if function identifies an isogram
    def test_solve_function(self):
        word = 'ashshsa'
        answer = is_isogram(word)
        expected = False
        self.assertEqual(answer, expected)

    # test to see if function counts spaces as a character
    def test_raise_error(self):
        word = "Woah      "
        answer = is_isogram(word)
        expected = True
        self.assertEqual(answer, expected)

    # test to see if function works with integer data types
    def test_removing_spaces_from_string(self):
        word = 12
        answer = is_isogram(word)
        expected = True
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()
