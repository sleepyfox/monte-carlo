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
		self.lines = open(filename).read().split('\n')
		self.lines = self.lines[:-1]

		self.temp_lines = []
		for line in self.lines:
			self.temp_lines.append(list(map(int, line.split(','))))
		self.lines = self.temp_lines

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
	def test_that_test_file_should_have_one_line(self):
		"When we try and read a small test file we get one row"
		myProjectData = ProjectFileReader("small-test-file.csv")
		self.assertEqual(len(myProjectData.lines), 1)

	def test_project_data_has_story_point_size(self):
		"From a single row test data file, we have a numerical Story Point"
		myProjectData = ProjectFileReader("small-test-file.csv")
		self.assertEqual(myProjectData.lines[0][0], 25)

if __name__ == "__main__":
	unittest.main()
