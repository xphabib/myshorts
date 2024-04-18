import os
import random
import subprocess

def merge_videos(videos, myclips):
    merged = []
    for i in range(0, (len(videos))):
        merged.append(videos[i])
        merged.append(myclips[i])
    return merged

def create_final_video_with_background_music(video_files, myclips, output_file, width, height):
    video_clips = [f"./videos/{file}" for file in video_files]
    video_myclips = [f"./myclips/{file}" for file in myclips]
    merge_clips = merge_videos(video_clips, video_myclips)

    input_args = " ".join([f"-i {file}" for file in merge_clips])
    filter_complex = ";".join([f"[{i}:v] setpts=PTS-STARTPTS, scale={width}:{height} [v{i}]; [{i}:a] asetpts=PTS-STARTPTS [a{i}]" for i in range(len(merge_clips))])
    concat_args = "".join([f"[v{i}][a{i}]" for i in range(len(merge_clips))])
    output_args = f"-map \"[out]\" -c:v libx264 -c:a aac -preset fast -shortest -y ./outputs/{output_file}"

    ffmpeg_command = f"ffmpeg {input_args} -filter_complex \"{filter_complex}{concat_args}concat=n={len(merge_clips)}:v=1:a=1[out]\" {output_args}"
    subprocess.run(ffmpeg_command, shell=True)

# Example usage
videos_path = './videos/'
videos_list = os.listdir(videos_path)
video_files = random.sample(videos_list, 5)
output_file = "final_output.mp4"
myclips = os.listdir('./myclips')

create_final_video_with_background_music(video_files, myclips, output_file, width=1920, height=1080)
