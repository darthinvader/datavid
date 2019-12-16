import moviepy.editor as mpy


def runner(function, duration, filename, fps, audio=None):
    clip = mpy.VideoClip(function, duration=duration)

    # if the audio exists
    if audio is not None:
        # then open the audiofile and add it to the video
        audio_clip = mpy.AudioFileClip(audio)
        audio_clip.set_duration(clip.duration)
        clip.audio = audio_clip

    # write the videofile
    clip.write_videofile(filename, fps=fps)
