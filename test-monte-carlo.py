"A test suite for a Monte-Carlo simulator"

import unittest
from monte_carlo import *

ESTIMATES = {
  "small": 7,
  "medium": 5,
  "large": 4
}


class ListSamplerSuite(unittest.TestCase):
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


class FileReaderSuite(unittest.TestCase):
	def test_that_test_file_should_have_one_line(self):
		"When we try and read a small test file we get one row"
		myProjectData = ProjectFileReader("small-test-file.csv")
		self.assertEqual(len(myProjectData.lines), 1)

	def test_project_data_has_story_point_size(self):
		"From a single row test data file, we have a numerical Story Point"
		myProjectData = ProjectFileReader("small-test-file.csv")
		self.assertEqual(myProjectData.lines[0][0], 25)

	def test_project_data_has_story_time_value(self):
		"From a single row test data file, we have a time value associated with a Story Point"
		myProjectData = ProjectFileReader("small-test-file.csv")
		self.assertEqual(myProjectData.lines[0][1], 376200)

	def test_that_real_file_should_have_259_lines(self):
		"When we try and read a small test file we get one row"
		myProjectData = ProjectFileReader("project-stats.csv")
		self.assertEqual(len(myProjectData.lines), 259)


class ProjectAnalyserSuite(unittest.TestCase):
	def test_empty_work_list_has_correct_categories(self):
		"Given an empty list of project data, work distribution has all three categories"
		myProjectData = ProjectFileReader("project-stats.csv")
		myProjectAnalysis = analyse(myProjectData)
		self.assertIn('small', myProjectAnalysis)
		self.assertIn('medium', myProjectAnalysis)
		self.assertIn('large', myProjectAnalysis)


if __name__ == "__main__":
	unittest.main()
