'Run 10000 simulations of the project, prints results to STDOUT'

import sys
from monte_carlo import *

SMALL_ESTIMATES = { 'small': 5 }
ESTIMATES = {
  'small': 7,
  'medium': 5,
  'large': 4
}

if sys.argv[1] == 'small':
    # Small project with only one category
    project = ProjectFileReader('../task-times.csv')
    analysis = analyse(project.lines)
    effort_list = simulate(analysis, SMALL_ESTIMATES, 100)
elif sys.argv[1] == 'large':
    # Large project with Story Point mappings
    project = ProjectFileReader('../project-stats.csv')
    analysis = analyse(project.lines)
    effort_list = simulate(analysis, ESTIMATES, 10000)
else:
    print('usage: run_simulation.py arg')
    print("    arg is either 'small' or 'large'")
    sys.exit()

for i in effort_list:
    print i
