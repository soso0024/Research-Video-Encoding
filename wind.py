import subprocess
import time

input_file = "/usr/local/bin/Netflix_WindAndNature_4096x2160_60fps_10bit_420.y4m"
output_file = "Netflix_WindAndNature.mp4"
resolution = "1920x1080"
codec = "libx264"

start_time = time.time()

# FFmpegコマンドの作成
ffmpeg_cmd = f"/usr/local/bin/ffmpeg-6.0-amd64-static/./ffmpeg -i {input_file} -s {resolution} -c:v {codec} {output_file}"

# FFmpegの実行
subprocess.call(ffmpeg_cmd, shell=True)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"エンコード時間: {elapsed_time}秒")