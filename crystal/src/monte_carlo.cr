module MonteCarlo

  def self.extract_task_times(file_contents : Array(String))
    file_contents.map { |x| x.split(',').last.to_i }
  end

  # TODO: allow random to be injected
  def self.sample(data : Array)
    data[Random.rand(data.size)]
  end

  def self.task_time(data : Array)
    (1..5).map { sample(data) }.sum
  end

  class Simulation
    include MonteCarlo
    @sim_data : Array(Int32)
    def initialize(data : Array)
      @sim_data = (1..100).map { MonteCarlo.task_time(data) }
    end
    def confidence_interval(percent)
      @sim_data[50]
    end
    def size
      @sim_data.size
    end
  end
end
