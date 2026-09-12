import unittest
from p5_Williams_Vincente import caesar_cipher, caesar_decipher, letter_frequency


class TestCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(caesar_cipher("abc", 1), "bcd")
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

    def test_decrypt(self):
        self.assertEqual(caesar_decipher("bcd", 1), "abc")
        self.assertEqual(caesar_decipher("Khoor", 3), "Hello")

    def test_roundtrip(self):
        original = "The quick brown fox!"
        self.assertEqual(caesar_decipher(caesar_cipher(original, 7), 7), original)


class TestFrequency(unittest.TestCase):
    def test_count(self):
        freq = letter_frequency("aabbbcccc")
        self.assertEqual(freq["a"], 2)
        self.assertEqual(freq["b"], 3)
        self.assertEqual(freq["c"], 4)

    def test_case_and_punctuation(self):
        freq = letter_frequency("AaA! 123")
        self.assertEqual(freq["a"], 3)

    def test_empty(self):
        self.assertEqual(letter_frequency(""), {})


if __name__ == "__main__":
    unittest.main()