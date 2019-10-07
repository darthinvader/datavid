from PIL import Image
from FrameProcessing.FrameItem import FrameItem
import bisect


class ImageItem(FrameItem):
    def __init__(self, image_path, width, height, x=0, y=0, order=1):
        super().__init__(width, height, x, y, order)
        self.image = image_path
        self.rendering_image = None
        self.change_image = True
        self.frame_items = list()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image_path):
        self.__image = Image.open(image_path)
        self.change_image = True

    @property
    def rendering_image(self):
        return self.__rendering_image

    @rendering_image.setter
    def rendering_image(self, rendering_image):
        self.__rendering_image = rendering_image

    @property
    def change_image(self):
        return self.__change_image

    @change_image.setter
    def change_image(self, change_image):
        self.__change_image = change_image

    @property
    def frame_items(self):
        return self.__frame_items

    @frame_items.setter
    def frame_items(self, frame_items):
        self.__frame_items = frame_items
        self.change_image = True

    def add_frame_item(self, frame_item):
        bisect.insort(self.frame_items, frame_item)
        self.change_image = True

    def remove_frame_item(self, ID):
        for fi in self.__frame_items:
            if id(fi) == ID:
                self.__frame_items.remove(fi)
                self.change_image = True

    def render(self, image):
        if self.change_image:
            self.rendering_image = self.image.resize((self.width, self.height))
            for fi in self.frame_items:
                fi.render(self.rendering_image)
        image.paste(self.rendering_image)
        self.change_image = False
