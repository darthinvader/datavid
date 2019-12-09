from FrameProcessing.FrameItem import FrameItem
from PIL import Image


class ImageItem(FrameItem):
    def __init__(self, image_path, width, height, x=0, y=0):
        super().__init__(width, height, x, y)
        self.image = image_path
        self.rendering_image = None
        self.change_image = True

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image_path):
        self.__image = Image.open(image_path).convert('RGBA')
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

    def render(self, image):
        pass
