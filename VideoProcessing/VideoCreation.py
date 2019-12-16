import moviepy.editor as mpy


def runner(function, duration, filename, fps, audio=None):
    clip = mpy.VideoClip(function, duration=duration)

    # if the audio exists
    if audio is not None:
        # If the audio is a list
        if type(audio) is list:
            audio_clip_list = list()
            # Then we add all the audiofiles
            for audio_file in audio:
                if audio_file is str:
                    temp_audio_clip = mpy.AudioFileClip(audio)
                elif audio_file is mpy.AudioClip:
                    temp_audio_clip = mpy.AudioFileClip(audio)
                else:
                    raise Exception(
                        "Parameter audio that was passed as a list containing elements of incorrect variable type. "
                        "Type must either be a filename string or a moviepy.Audioclip.")

                audio_clip_list.append(temp_audio_clip)
            # We then merge the audiofiles
            audio_clip = mpy.CompositeAudioClip(audio_clip_list)

        elif type(audio) is str:
            audio_clip = mpy.AudioFileClip(audio)

        elif type(audio) is mpy.AudioClip:
            audio_clip = audio
        else:
            raise Exception(
                "Parameter audio is incorrect type of variable. Type must either a filename string, "
                "a moviepy. Audioclip or  list of moviepy.Audioclip or filename string.")

        audio_clip = audio_clip.set_duration(clip.duration)
        clip.audio = audio_clip

    clip.write_videofile(filename, fps=fps)
