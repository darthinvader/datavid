import moviepy.editor as mpy


def runner(function, duration, filename, fps, audio=None):
    clip = mpy.VideoClip(function, duration=duration)

    # if the audio exists
    if audio is not None:
        set_clip_audio(audio, clip)

    clip.write_videofile(filename, fps=fps)


def set_clip_audio(audio, clip):
    # If the audio is a list
    if type(audio) is list:
        audio_clip = audio_list_combine(audio)

    elif type(audio) is str:
        audio_clip = mpy.AudioFileClip(audio)

    elif type(audio) is mpy.AudioClip:
        audio_clip = audio
    else:
        raise Exception(
            "Parameter audio is incorrect type of variable. Type must either a filename string, "
            "a moviepy.Audioclip or a list of moviepy.Audioclip or filename strings.")
    audio_clip = audio_clip.set_duration(clip.duration)
    clip.audio = audio_clip


def audio_list_combine(audio):
    audio_clip_list = list()
    # We add all the audiofiles to a list
    for audio_file in audio:
        if type(audio_file) is str:
            temp_audio_clip = mpy.AudioFileClip(audio_file)
        elif type(audio_file) is mpy.AudioClip:
            temp_audio_clip = audio_file
        else:
            raise Exception(
                "Parameter audio that was passed as a list containing elements of incorrect variable type. "
                "Type must either be a filename string or a moviepy.Audioclip.")

        audio_clip_list.append(temp_audio_clip)
    # We then merge the audiofiles
    audio_clip = mpy.CompositeAudioClip(audio_clip_list)
    return audio_clip
