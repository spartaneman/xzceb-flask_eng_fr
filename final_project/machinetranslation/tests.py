"""Module to conduct unit testing"""

import unittest

from translator import french_to_english, english_to_french

#Test that the translation works from French to English
class TestFrenchToEnglish(unittest.TestCase):
    def test_1(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertEqual(french_to_english('soleil'), 'sun')

#Test that the translation works from English to French
class TestEnglishToFrench(unittest.TestCase):
    def test_2(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french('sun'), 'soleil')

unittest.main()