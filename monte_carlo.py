import random

ALL_BUT_LAST = -1
COMMA = ','
NEWLINE = '\n'

def analyse(project_stats):
	"""Takes a list of pairs of (Story points, time in minutes)
	   Returns a map of lists of time in minutes grouped by
	   (small|medium|large)"""
	analysis_map = { 'small': [], 'medium': [], 'large': [] }
	for story_points, time in project_stats:
		analysis_map['small'].append(time)
	return analysis_map

class WorkItemList():
	def __init__(self, xs):
		self.list = xs

	def pickItemFromList(self):
		'picks a single work item at random from a list'
		return random.choice(self.list)

	def sample(self, times):
		'returns a series of random samples from a list'
		return [self.pickItemFromList() for i in range(times)]


class ProjectFileReader():
	def __init__(self, filename):
		'''Takes a CSV file name, reads it in and
		   Returns a list of pairs of numbers'''

		def parseWorkItem(line_of_text):
			return list(map(int, line_of_text.split(COMMA)))

		with open(filename) as f:
			lines = f.read().split(NEWLINE)[:ALL_BUT_LAST]
			self.lines = [parseWorkItem(line) for line in lines]
