module MonteCarlo

  def self.extract_task_times(file_contents : Array(String))
    file_contents.map { |x| x.split(',').last.to_i }
  end

  def self.sample(task_times_in_seconds : Array, randomiser)
    task_times_in_seconds[randomiser.rand(task_times_in_seconds.size)]
  end

  def self.overall_time(task_times_in_seconds : Array, randomiser)
    (1..5).map { sample(task_times_in_seconds, randomiser) }.sum
  end

  class Simulation
    @sim_data : Array(Int32)
    def initialize(data : Array, randomiser = Random.new)
      @sim_data = (1..100).map { MonteCarlo.overall_time(data, randomiser) }.sort
    end
    def confidence_interval(percent)
      @sim_data[(size * percent).to_i]
    end
    def size
      @sim_data.size
    end
  end
end
