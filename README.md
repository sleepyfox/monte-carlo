# Monte-Carlo Kata
This is a worked example in Python based upon the Monte-Carlo kata.

Run the tests with:

    python test-monte-carlo.py

The source of the kata is the code dojo that @sleepyfox ran for the London Code Dojo [link]()

The text of the kata at the link above is reproduced below:

# Kata definition
Our business has a historical data set containing the time taken to complete tasks in seconds, the file is in CSV format and the first field is a placeholder - always '1'. The file can be downloaded [here](http://j.mp/task-times).

Our new mini-project consists of 5 tasks. In order to get an estimate of how long it will take to deliver, we can draw a random sample of 5 entries from our dataset.

If we take enough samples, then the distribution of results will tell us something about how long our project is likely to take.

## Exercise 1
Do this sampling 100 times and use the data to draw a graph of the distribution (you can use a spreadsheet or other canned mechanism for this).  The mid-point of the histogram will give us a 50% confidence interval, and if we order the results by size then the 80th result will give us an 80% confidence interval estimate.

## Exercise 2
Our business has more historical data on how long tasks take in seconds, grouped by story size in points. Data set available [here](http://j.mp/story-sizes).

We are about to begin a larger project, which we have done some T-shirt sizing on (S, M or L) and we've correlated these T-shirt sizes to story point estimates.

Use the Monte-Carlo Method to estimate how long the project will take, given that we have:
* 7 Small stories (1-3 points)
* 5 Medium stories (5-8 points)
* 4 Large stories (13 points and above)

Use 10,000 runs of the simulator and output the data to a histogram as before.
