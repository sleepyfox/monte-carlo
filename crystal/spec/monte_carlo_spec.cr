require "spec"
require "../src/monte_carlo"

class FakeRand
  def rand(n)
    (0.5 * n).to_i
  end
end

describe "Monte Carlo" do
  describe "A file reader" do
    it "reads the first line of the file" do
      content = File.read_lines("./task-times.csv")
      content[0].should eq "1,3600"
    end

    it "can extract the time in seconds" do
      content = File.read_lines("./task-times.csv")
      MonteCarlo.extract_task_times(content)[0].should eq 3600
    end
  end

  describe "A sampler" do
    it "can pick an item at random from a list" do
      MonteCarlo.sample([1, 1, 1], Random.new).should eq 1
    end
  end

  describe "A new task" do
    it "should last five seconds" do
      MonteCarlo.overall_time([1, 1, 1], Random.new).should eq 5
    end
  end

  describe "A simulation" do
    it "should have 100 task samples" do
      MonteCarlo::Simulation.new([1,1,1]).size.should eq 100
    end
  end

  describe "A confidence interval" do
    fake_rand = FakeRand.new

    it "should be able to determine the median" do
      sim = MonteCarlo::Simulation.new([1,1,1])
      sim.confidence_interval(0.50).should eq 5
    end
    it "should be able to handle larger data sets" do
      sim = MonteCarlo::Simulation.new([0,1,2,3,4,5,6,7,8,9], fake_rand)
      sim.confidence_interval(0.50).should eq 25
    end
    it "should be able to find 90% confindence interval" do
      sim = MonteCarlo::Simulation.new([1,1,1])
      sim.confidence_interval(0.90).should eq 5
    end
  end
end
