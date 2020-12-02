# Monte-Carlo kata

This code kata was used in the 36th meeting of the [London Code Dojo](https://www.meetup.com/London-Code-Dojo/events/229432041/).

# Kata definition

Our business has a historical data set containing the time taken to complete tasks in seconds, the file is in CSV format and the first field is a placeholder - always '1'. The file can be downloaded [here](./task-times.csv).

Our new mini-project consists of 5 tasks. In order to get an estimate of how long it will take to deliver, we can draw a random sample of 5 entries from our dataset.

If we take enough samples, then the distribution of results will tell us something about how long our project is likely to take.

Do this sampling 100 times. If you were to use the data to draw a histogram of the distribution e.g. using a s spreadsheet, the mid-point of the histogram will give us a 50% confidence interval, and if we order the results by size then the 80th result will give us an 80% confidence interval estimate.

Produce 50th and 80th percentile confidence intervals for how long you think the task will take.

When you've finished this, you can move onto the second part of the exercise [here](./README_2nd.md)
