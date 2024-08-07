import moviepy.editor 

video = moviepy.editor.VideoFileClip('video.mp4')

audio = video.audio

audio.write_audiofile('audio.mp3')