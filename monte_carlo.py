import random

ALL_BUT_LAST = -1

def analyse(project_stats):
	"""Takes a list of pairs of (Story points, time in minutes)
	   Returns a map of lists of time in minutes grouped by
	   (small|medium|large)"""
	return { 'small': 1, 'medium': 1, 'large': 1}

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
		def parseWorkItem(line_of_text):
			return list(map(int, line_of_text.split(',')))

		with open(filename) as f:
			lines = f.read().split('\n')[:ALL_BUT_LAST]
			self.lines = [parseWorkItem(line) for line in lines]
