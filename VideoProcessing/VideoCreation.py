import moviepy.editor as mpy


def runner(function, filename, fps, duration):
    clip = mpy.VideoClip(function, duration=duration)
    clip.write_videofile(filename, fps=fps)
