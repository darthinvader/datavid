from abc import ABC, abstractmethod


class Effect(ABC):
    def __init__(self, shape=None):
        self.shape = None

    @abstractmethod
    def add_shape(self, shape):
        pass

    @abstractmethod
    def apply_effect(self, current_frame):
        pass
