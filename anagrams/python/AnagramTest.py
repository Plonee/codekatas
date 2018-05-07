import unittest

from python.Anagram import Anagram


class TestAnagram(unittest.TestCase):

    def setUp(self):
        self.anagram = Anagram('something')

    def test_innerText(self):
        self.assertEqual(self.anagram.inner_text, 'something')

    def test_repr(self):
        self.assertEqual(self.anagram.__repr__(), 'inner: something')
