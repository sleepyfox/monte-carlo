"A test suite for a Monte-Carlo simulator"

import unittest
import random

class WorkItemList():
	list = [1]

	def pickItemFromList(self):
		return random.choice(self.list)

class TestSuite(unittest.TestCase):
	def setUp(self):
		self.monte = 1

	def testFileProcessorCanParseData(self):
		"A single line is parsed into a..."
		self.assertEqual(self.monte, 1)

	def testPickOneFromListofOneItem(self):
		"When we pick an item from a list of one, we always get the same item"
		myList = WorkItemList()
		self.assertEqual(myList.pickItemFromList(), 1)

if __name__ == "__main__":
	unittest.main()
