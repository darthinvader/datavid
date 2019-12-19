from PIL import Image

from datavid.FrameProcessing.BasicItems.FrameItem import FrameItem


class ImageItem(FrameItem):
    def __init__(self, image_path, width, height, x=0, y=0):
        super().__init__(width, height, x, y)
        self.image = image_path

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image_path):
        self.__image = Image.open(image_path).convert('RGBA').resize((self.width, self.height))

    def render(self, image):
        image.paste(self.image, (self.x, self.y), mask=self.image)
