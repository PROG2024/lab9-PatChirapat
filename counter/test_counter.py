"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter

class TestCounter(unittest.TestCase):

   def setUp(self):
      self.counter1 = Counter()
      self.counter2 = Counter()

   def test_singleton(self):
      self.assertIs(self.counter1, self.counter2)

   def test_increment(self):
      self.counter1.increment()
      self.assertEqual(self.counter1.count, 1)
      self.assertEqual(self.counter2.count, 1)
