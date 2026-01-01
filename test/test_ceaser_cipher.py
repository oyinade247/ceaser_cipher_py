from unittest import TestCase
from src.ceaser_cipher import encrypt, decrypt




class Test(TestCase):
    def test_that_word_can_be_encrypted(self):
        word = "hello"
        key = 2
        actual = encrypt(word, key)
        expected = "jgnnq"
        self.assertEqual(actual, expected)


    def test_that_word_in_capital_letters_can_be_encrypted(self):
         word = "HELLO"
         key = 2
         actual = encrypt(word, key)
         expected = "JGNNQ"
         self.assertEqual(actual, expected)

    def test_that_word_can_be_decrypted(self):
        word = "hello"
        key = 2
        actual = decrypt(word, key)
        expected = "fcjjm"
        self.assertEqual(actual, expected)

    def test_that_word_in_capital_letters_can_be_decrypted(self):
        word = "HELLO"
        key = 2
        actual = decrypt(word, key)
        expected = "FCJJM"
        self.assertEqual(actual, expected)
