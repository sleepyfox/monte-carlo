require "spec"

def extract_task_times(file_contents : Array(String))
  file_contents.map { |x| x.split(',').last.to_i }
end

describe "Monte Carlo" do
  describe "File reader" do
    it "reads the first line of the file" do
      content = File.read_lines("./task-times.csv")
      content[0].should eq "1,3600"
    end
    it "can extract the time in seconds" do
      content = File.read_lines("./task-times.csv")
      extract_task_times(content)[0].should eq 3600
    end
  end
end
