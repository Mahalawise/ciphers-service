from django.test import TestCase
from .ciphers import caesar_encode

# Create your tests here.
class CiphersTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = 'hello'
        shift = 1
        expected = 'ifmmp'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected,output)