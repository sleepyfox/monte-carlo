"A test suite for a Monte-Carlo simulator"

import unittest
import random

class WorkItemList():
	def __init__(self, xs):
		self.list = xs

	def pickItemFromList(self):
		"picks a single work item at random from a list"
		return random.choice(self.list)

	def sample(self, times):
		"returns a series of random samples from a list"
		return [1 for i in range(times)]

class TestSuite(unittest.TestCase):
	# def setUp(self):
	# 	self.monte = 1
	#
	# def test_file_processor_can_parse_data(self):
	# 	"A single line is parsed into a..."
	# 	self.assertEqual(self.monte, 1)

	def test_pick_from_list_of_one_item(self):
		"When we pick an item from a list of one, we always get the same item"
		myList = WorkItemList([1])
		self.assertEqual(myList.pickItemFromList(), 1)

	def test_sample_of_10_items(self):
		"When we ask for ten samples from a list then we get 10 items"
		myList = WorkItemList([2])
		self.assertEqual(len(myList.sample(10)), 10)

if __name__ == "__main__":
	unittest.main()
