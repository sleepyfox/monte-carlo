module MonteCarlo

  def self.extract_task_times(file_contents : Array(String))
    file_contents.map { |x| x.split(',').last.to_i }
  end

  def self.sample(data : Array)
    data[Random.rand(data.size)]
  end

  def self.task_time(data : Array)
    (1..5).map { sample(data) }.sum
  end

  def self.simulation(data : Array)
    (1..100).map { task_time(data) }
  end

  def self.confidence_interval(data, interval_percent)
    if (interval_percent < 0.0 || interval_percent > 1.0)
      raise "interval should be between 0.01 and 1.00"
    end
    pick = (data.size * interval_percent).round.to_i
    data.sort[pick - 1]
  end
end
