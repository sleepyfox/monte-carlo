require "./monte_carlo"

def in_days(seconds)
  (seconds / (3600 * 24)).round(1)
end

content = File.read_lines("./task-times.csv")
timings = MonteCarlo.extract_task_times(content)
sim = MonteCarlo.simulation(timings)
sim.each { |x| puts x }
# print 50th and 90th percentile confidence intervals
ci50 = MonteCarlo.confidence_interval(sim, 0.5)
ci90 = MonteCarlo.confidence_interval(sim, 0.9)
puts "50% confidence #{ci50}s = #{in_days(ci50)}"
puts "90% confidence #{ci90}s = #{in_days(ci90)}"
