require "spec"

def extract_task_times(file_contents : Array(String))
  file_contents.map { |x| x.split(',').last.to_i }
end

def sample(data : Array)
  data[Random.rand(data.size)]
end

def task_time(data : Array)
  (1..5).map { sample(data) }.sum
end

def simulation(data)
  (1..100).map { task_time(data) }
end

describe "Monte Carlo" do
  describe "A file reader" do
    it "reads the first line of the file" do
      content = File.read_lines("./task-times.csv")
      content[0].should eq "1,3600"
    end

    it "can extract the time in seconds" do
      content = File.read_lines("./task-times.csv")
      extract_task_times(content)[0].should eq 3600
    end
  end

  describe "A sampler" do
    it "can pick an item at random from a list" do
      sample([1, 1, 1]).should eq 1
    end
  end

  describe "A new task" do
    it "should last five seconds" do
      task_time([1, 1, 1]).should eq 5
    end
  end

  describe "A simulation" do
    it "should have 100 task samples" do
      simulation([1, 1, 1]).size.should eq 100
    end
  end
end
