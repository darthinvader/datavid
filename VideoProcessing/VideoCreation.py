import moviepy.editor as mpy


def runner(function, duration, filename, fps, audio=None):
    clip = mpy.VideoClip(function, duration=duration)

    # if the audio exists
    if audio is not None:
        wrong_audio_type = False
        if type(audio) is list:
            audio_clip_list = list()
            for audio_file in audio:
                temp_audio_clip = mpy.AudioFileClip(audio)
                audio_clip_list.append(temp_audio_clip)
            audio_clip = mpy.CompositeAudioClip(audio_clip_list)

        elif type(audio) is str:
            audio_clip = mpy.AudioFileClip(audio)

        elif type(audio) is mpy.AudioClip:
            audio_clip = audio
        else:
            raise Exception("Parameter audio is incorrect type of variable.")

        audio_clip = audio_clip.set_duration(clip.duration)
        clip.audio = audio_clip

    clip.write_videofile(filename, fps=fps)
