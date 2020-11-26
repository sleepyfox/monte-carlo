require "spec"
require "file"

describe "Monte Carlo" do
  describe "File reader" do
    it "reads the first line of the file" do
      content = File.read_lines("./task-times.csv")
      content[0].should eq "1,3600"
    end
    it "can extract the time in seconds" do
      content = File.read_lines("./task-times.csv")
      content[0].split(",")[1].to_i.should eq 3600
    end
  end
end
