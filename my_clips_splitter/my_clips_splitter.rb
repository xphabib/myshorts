require 'roo'
xlsx_file = 'input.xlsx'
xlsx = Roo::Spreadsheet.open(xlsx_file)
xlsx.default_sheet = xlsx.sheets.first
times_arr = []
xlsx.each_row_streaming(offset: 1) do |row|
    time_hash = {}
    if !row[0].value.nil?
        time_hash[:start] = row[0].value
        time_hash[:end] = row[1].value
        times_arr << time_hash
    else
        break
    end
end

output_directory = "../short_maker/myclips"

files = Dir.glob(File.join(output_directory, '*'))
file_count = files.count

times_arr.each_with_index do |time, index|
    system("ffmpeg -i input.mp4 -ss #{time[:start]} -to #{time[:end]} -c:v libx264 -c:a aac #{output_directory}/clip_#{file_count+index+1}.mp4")
end
