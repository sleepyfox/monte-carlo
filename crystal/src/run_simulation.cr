require "./monte_carlo"

# Convert seconds to days with 2 significant digits
def in_days(seconds)
  (seconds / (3600 * 24)).round(1)
end

content = File.read_lines("./task-times.csv")
timings = MonteCarlo.extract_task_times(content)
sim = MonteCarlo::Simulation.new(timings)

# Output all sim values for spreadsheet
# sim.each { |x| puts x }

# print 50th and 90th percentile confidence intervals
ci50 = sim.confidence_interval(0.5)
ci80 = sim.confidence_interval(0.8)
ci90 = sim.confidence_interval(0.9)
ci98 = sim.confidence_interval(0.98)
puts "50% confidence #{ci50}s = #{in_days(ci50)}d"
puts "80% confidence #{ci80}s = #{in_days(ci80)}d"
puts "90% confidence #{ci80}s = #{in_days(ci90)}d"
puts "98% confidence #{ci98}s = #{in_days(ci98)}d"
