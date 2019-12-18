from FrameProcessing.ShapeEffects.Effect import Effect


class Fade(Effect):
    def __init__(self, shape=None, starting_frame=0, ending_frame=100, target_opacity=0):
        super(Fade, self).__init__()
        self.starting_frame = starting_frame
        self.ending_frame = ending_frame
        self.target_opacity = target_opacity
        if shape is None:
            self.starting_opacity = None
        else:
            self.starting_opacity = self.shape.fill_color[3]
            self.opacity_change_per_frame = self.calculate_opacity_change(ending_frame, starting_frame, target_opacity)
        self.target_opacity = target_opacity

    def calculate_opacity_change(self, ending_frame, starting_frame, target_opacity):
        opacity_difference = self.starting_opacity - target_opacity
        frame_difference = ending_frame - starting_frame
        return opacity_difference / frame_difference

    def add_shape(self, shape):
        self.shape = shape
        self.starting_opacity = self.shape.fill_color[3]
        self.opacity_change_per_frame = (self.starting_opacity - self.target_opacity) / (
                self.ending_frame - self.starting_frame)

    def apply_effect(self, current_frame):
        if current_frame < self.starting_frame or current_frame > self.ending_frame:
            return False
        frames_past = current_frame - self.starting_frame
        current_opacity = self.starting_opacity - (self.opacity_change_per_frame * frames_past)
        new_fill_color = list(self.shape.fill_color)
        new_fill_color[3] = int(current_opacity)
        self.shape.fill_color = tuple(new_fill_color)
        return True
