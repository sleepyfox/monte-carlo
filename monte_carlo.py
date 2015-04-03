import random

ALL_BUT_LAST = -1
COMMA = ','
NEWLINE = '\n'

def analyse(project_stats):
	'''Takes a list of pairs of (Story points, time in minutes)
	   Returns a map of categories (small|medium|large) to WorkItemLists'''
	analysis_map = {
		'small':   WorkItemList([]),
		'medium':  WorkItemList([]),
		'large':   WorkItemList([])
	}
	for story_points, effort in project_stats:
		if story_points <= 8:
			analysis_map['small'].append(effort)
		elif story_points <= 20:
			analysis_map['medium'].append(effort)
		else:
			analysis_map['large'].append(effort)
	return analysis_map

def simulate(project_analysis, estimates, runs):
	''' Takes a project analysis that is a map of WorkItemLists
		and a map of estimate categories and number of items
		and a number of runs of the simulator
		Returns a list of effort durations'''
	# smalls =

def total_effort(project_analysis, estimates):
	''' Takes a project analysis that is a map of WorkItemLists
		and a map of estimate categories and number of items
		Returns an effort based upon a random sampling of the analysis times the estimated number of work items'''
	total_effort = 0
	smalls = project_analysis['small']
	num_smalls = estimates['small']
	total_effort += sum(smalls.sample(num_smalls))
	mediums = project_analysis['medium']
	num_mediums = estimates['medium']
	total_effort += sum(mediums.sample(num_mediums))
	larges = project_analysis['large']
	num_larges = estimates['large']
	total_effort += sum(larges.sample(num_larges))
	return total_effort


class WorkItemList():
	def __init__(self, xs):
		self.list = xs

	def pickItemFromList(self):
		'picks a single work item at random from a list'
		return random.choice(self.list)

	def sample(self, times):
		'returns a series of random samples from a list'
		return [self.pickItemFromList() for i in range(times)]

	def append(self, item):
		'adds an item to the end of the list'
		self.list.append(item)
		return len(self.list)


class ProjectFileReader():
	def __init__(self, filename):
		'''Takes a CSV file name, reads it in and
		   Returns a list of pairs of numbers'''

		def parseWorkItem(line_of_text):
			return list(map(int, line_of_text.split(COMMA)))

		with open(filename) as f:
			lines = f.read().split(NEWLINE)[:ALL_BUT_LAST]
			self.lines = [parseWorkItem(line) for line in lines]
