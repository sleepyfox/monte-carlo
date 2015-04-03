'Run 10000 simulations of the project, prints results to STDOUT'

from monte_carlo import *

ESTIMATES = {
  'small': 7,
  'medium': 5,
  'large': 4
}

myProjectData = ProjectFileReader('project-stats.csv')
myProjectAnalysis = analyse(myProjectData.lines)
effort_list = simulate(myProjectAnalysis, ESTIMATES, 10000)
for i in effort_list:
    print(i)
