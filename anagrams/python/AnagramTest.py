import unittest

from python.Anagram import Anagram


class TestAnagram(unittest.TestCase):

    def setUp(self):
        self.anagram = Anagram('something')

    def test_upper(self):
        self.assertEqual(1,1)

