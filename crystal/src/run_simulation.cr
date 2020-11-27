require "./monte_carlo"

content = File.read_lines("./task-times.csv")
timings = MonteCarlo.extract_task_times(content)
sim = MonteCarlo.simulation(timings)
sim.each { |x| puts x }
