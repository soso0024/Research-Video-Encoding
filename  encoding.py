import subprocess
import time

input_file = "/usr/local/bin/video_name"
output_file = "file_name.mp4"
resolution = "1920x1080"
codec = "libx264"

start_time = time.time()

ffmpeg_cmd = f"/usr/local/bin/ffmpeg-6.0-amd64-static/./ffmpeg -i {input_file} -s {resolution} -c:v {codec} {output_file}"

subprocess.call(ffmpeg_cmd, shell=True)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"エンコード時間: {elapsed_time}秒")