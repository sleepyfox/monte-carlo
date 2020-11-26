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

  def self.simulation(data)
    (1..100).map { task_time(data) }
  end

end
