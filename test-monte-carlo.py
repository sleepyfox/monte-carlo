"A test suite for a Monte-Carlo simulator"

import unittest

class TestSuite(unittest.TestCase):
	def setUp(self):
		self.monte = 1

	def test1isI(self):
		"1 is equal to 1"
		self.assertEqual(self.monte, 1)

if __name__ == "__main__":
	unittest.main()
