from unittest import TestCase, main
from eng_vowels.vowels import count_vowels


class CountVowelsTest(TestCase):
    def test_all_vowels(self):
        self.assertEqual(count_vowels('ooo'), 3)

    def test_no_vowels(self):
        self.assertEqual(count_vowels('bcd'), 0)

    def test_digits(self):
        self.assertEqual(count_vowels('0o0'), 1)

    def test_lower(self):
        self.assertEqual(count_vowels('s.aeiou.s'), 5)

    def test_upper(self):
        self.assertEqual(count_vowels('S.AEIOU.S'), 5)

    def test_non_ascii(self):
        self.assertEqual(count_vowels('äöüß'), 0)

    def test_empty_string(self):
        self.assertEqual(count_vowels(''), 0)


if __name__ == '__main__':
    main()