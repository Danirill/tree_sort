import unittest
from sort_tree import treesort as sort

class TestStringMethods(unittest.TestCase):

  def test_empty(self):
      self.assertEqual(sort([]), [])

  def test_one_element_array(self):
      self.assertEqual(sort(["a"]), ["a"])

  def test_simple_strings(self):
      self.assertEqual(sort(["b", "a", "c"]), ["a", "b", "c"])

  def test_numbers(self):
      self.assertEqual(sort(["3", "1", "2"]), ["1", "2", "3"])

  def test_simple_strings_different_cases(self):
      self.assertEqual(sort(["a", "A", "B", "b"]), ["A", "B", "a", "b"])

  def test_simple_strings_special_character(self):
      self.assertEqual(sort(["a", "A", "!", "B"]), ["!", "A", "B", "a"])

  def test_simple_strings_special_character_and_numbers_and_cases(self):
      self.assertEqual(sort(["a", "5", "!", "B"]), ["!", "5", "B", "a"])

  def test_long_strings(self):
      self.assertEqual(sort(["aaa", "aba", "aab", "bba"]), ["aaa", "aab", "aba", "bba"])

  def test_long_strings_different_cases_1(self):
      self.assertEqual(sort(["Aaa", "aba", "Bab", "bba"]), ["Aaa", "Bab", "aba", "bba"])

  def test_long_strings_different_cases_2(self):
      self.assertEqual(sort(["bbF", "Aaa", "ABA", "Cba", "Bab", "bba"]), ["ABA", "Aaa", "Bab", "Cba", "bbF", "bba"])

  def test_long_strings_special_character(self):
      self.assertEqual(sort(["!", "a!", "@a!"]), ["!", "@a!", "a!"])

  def test_long_strings_special_character_different_cases(self):
      self.assertEqual(sort(["A!", "a!", "@a!"]), ["@a!", "A!", "a!"])

  def test_equal_elements(self):
      self.assertEqual(sort(["a", "a", "a"]), ["a", "a", "a"])

if __name__ == '__main__':
    unittest.main()