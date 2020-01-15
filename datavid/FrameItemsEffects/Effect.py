from abc import ABC, abstractmethod


class Effect:
    @abstractmethod
    def apply(self, frame_item):
        pass
