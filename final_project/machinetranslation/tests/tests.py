import unittest

from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test_null_en2fr(self):
        self.assertNotEqual(english_to_french(None), "Bonjour")
        self.assertEqual(english_to_french(None), "")

    def test_en2fr(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_null_fr2en(self):
        self.assertNotEqual(french_to_english(None), "Hello")
        self.assertEqual(french_to_english(None), "")

    def test_fr2en(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
