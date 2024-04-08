import moviepy
import moviepy.editor as mvd

# Get the file path
video = mvd.VideoFileClip(r"C:\\Users\\a.kazemi\Desktop\Arash\\GitProjects\10PythonBasicProjects\\Projects\\Extract Audio from Video\\Videos\big_buck.mp4")

# Convert Video to Audio
audio = video.audio
audio.write_audiofile(r'C:\\Users\\a.kazemi\Desktop\Arash\\GitProjects\10PythonBasicProjects\\Projects\\Extract Audio from Video\Audios\\audioconvert.mp3')