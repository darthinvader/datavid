from PIL import Image
import bisect


class MainFrame:
    def __init__(self, mode="RGB", dimensions=(3840, 2160), color=(0, 0, 0)):
        self.image = Image.new(mode, dimensions, color)
        self.frame_items = list()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    @property
    def frame_items(self):
        return self.__frame_items

    @frame_items.setter
    def frame_items(self, frame_items):
        self.__frame_items = frame_items

    def add_frame_item(self, frame_item):
        bisect.insort(self.frame_items, frame_item)

    def remove_frame_item(self, ID):
        for fi in self.__frame_items:
            if id(fi) == ID:
                self.__frame_items.remove(fi)

    def render(self):
        for fi in self.frame_items:
            fi.render(self.image)
