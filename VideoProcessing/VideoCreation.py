import moviepy.editor as mpy


def runner(function, duration, filename, fps, audio):
    clip = mpy.VideoClip(function, duration=duration)
    audio_clip = mpy.AudioFileClip(audio).set_duration(clip.duration)
    clip.audio = audio_clip
    clip.write_videofile(filename, fps=fps)
