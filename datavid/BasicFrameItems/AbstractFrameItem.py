from abc import ABC, abstractmethod
import math


class AbstractFrameItem(ABC):

    def __init__(self, x=0, y=0, current_frame=0, frame_added=None, frames_to_live=-1):
        self.x = x
        self.y = y
        self.current_frame = current_frame
        # If the frame_added is None then it means that the frame was added at the current frame
        if frame_added is None:
            self.frame_added = current_frame
        else:
            self.frame_added = frame_added
        self.effects = list()
        self.frames_to_live = frames_to_live

    def frames_alive(self):
        return self.current_frame - self.frame_added

    def increment_current_frame(self):
        self.current_frame += 1

    def is_dead(self):
        if self.frames_to_live == -1:
            return False
        if self.frames_alive() > self.frames_to_live:
            return True
        else:
            return False

    def add_effect(self, effect):
        self.effects.append(effect)

    def add_effects_list(self, effects):
        for effect in effects:
            self.add_effect(effect)

    def apply_effects(self):
        for effect in self.effects:
            effect.apply(self)

    def remaining_frames_to_live(self):
        if self.frames_to_live == -1:
            return math.inf
        else:
            return self.frames_to_live - self.frames_alive()

    @abstractmethod
    def render(self, image):
        pass
