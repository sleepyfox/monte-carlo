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
		return [self.pickItemFromList() for i in range(times)]

class ProjectFileReader():
	def __init__(self, filename):
		self.lines = [line.strip() for line in open(filename)]

class ListSampler(unittest.TestCase):
	def test_pick_from_list_of_one_item(self):
		"When we pick an item from a list of one, we always get the same item"
		myList = WorkItemList([1])
		self.assertEqual(myList.pickItemFromList(), 1)

	def test_sample_of_ten_has_ten_items(self):
		"When we ask for ten samples from a list then we get 10 results"
		myList = WorkItemList([2])
		self.assertEqual(len(myList.sample(10)), 10)

	def test_sample_of_ten_has_items_all__the_same(self):
		"When we ask for 10 samples from a list of one then we get 10 items all the same"
		myList = WorkItemList([3])
		self.assertEqual(myList.sample(10).count(3), 10)

class ProjectDataReader(unittest.TestCase):
	def test_can_read_test_file(self):
		"When we try and read a test file we get one row"
		myProjectData = ProjectFileReader("small-test-file.csv")
		self.assertEqual(len(myProjectData.lines), 1)

if __name__ == "__main__":
	unittest.main()
