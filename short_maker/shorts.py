import os
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos(videos, myclips):
    merged = []
    for i in range(0, (len(videos))):
        merged.append(videos[i])
        merged.append(myclips[i])
    return merged

def create_final_video_with_background_music(video_files, myclips, output_file):
    video_clips = [VideoFileClip("./videos/" + file) for file in video_files]
    video_myclips = [VideoFileClip("./myclips/" + file) for file in myclips]
    merge_clips = merge_videos(video_clips, video_myclips)

    print(len(video_clips))
    print(len(video_myclips))
    print(len(merge_clips))
    print(merge_clips)

    final_video = concatenate_videoclips(merge_clips)
    width = 1080
    height = 1920
    final_video_resized = final_video.resize((width, height))
    final_video_resized.write_videofile("./outputs/"+output_file, codec="libx264", audio_codec="aac", resolution=(1080, 1920))

# Example usage
videos_path = './videos/'
videos_list = os.listdir(videos_path)
video_files = random.sample(videos_list, 5)
output_file = "final_output.mp4"
myclips = os.listdir('./myclips')

create_final_video_with_background_music(video_files, myclips, output_file)
