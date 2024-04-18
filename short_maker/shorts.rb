
require 'securerandom'
myclips_dir = "./myclips"
videos_dir = "./videos"
myclips_files = Dir.glob(File.join(myclips_dir, "*"))
videos_files = Dir.glob(File.join(videos_dir, "*"))
myclips_random = myclips_files.sample(5)
videos_random = videos_files.sample(5)

input_files = ""
videos_random.each_with_index do |v, i|
    input_files = input_files + "-i #{v} -i #{myclips_files[i]} "
end

input_files = input_files[0..-2]

ffmpeg_command = "ffmpeg #{input_files} -filter_complex \"[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a][5:v][5:a][6:v][6:a][7:v][7:a][8:v][8:a][9:v][9:a]concat=n=10:v=1:a=1[v][a]\" -map \"[v]\" -map \"[a]\" output_combined.mp4"

system(ffmpeg_command)
