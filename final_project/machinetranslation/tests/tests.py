import unittest

from e2f_translator_function import englishToFrench
from f2e_translator_function import frenchToEnglish


class TestTranslator(unittest.TestCase):
    def test_null_en2fr(self):
        with self.assertRaises(ValueError):
            englishToFrench(None)

    def test_null_fr2en(self):
        with self.assertRaises(ValueError):
            frenchToEnglish(None)

    def test_en2fr(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_fr2en(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


unittest.main()
