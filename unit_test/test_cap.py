import unittest
import cap


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        results = cap.cap_text(text)
        self.assertEqual(results, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        results = cap.cap_text(text)
        self.assertEqual(results, 'Monty Python')


if __name__ == '__main__':
    unittest.main()
