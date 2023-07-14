"""Module to conduct unit testing"""

import unittest

from translator import frenchToEnglish, englishToFrench

#Test that the translation works from French to English
class TestFrenchToEnglish(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('sun'), 'soleil')

#Test that the translation works from English to French
class TestEnglishToFrench(unittest.TestCase):
    def test_2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('soleil'), 'sun')

unittest.main()