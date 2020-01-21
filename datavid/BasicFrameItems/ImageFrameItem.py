from PIL import Image

from datavid.BasicFrameItems.AbstractFrameItem import AbstractFrameItem


class ImageFrameItem(AbstractFrameItem):
    def __init__(self, image, width=3840, height=2160, x=0, y=0, current_frame=0, frame_added=None, frames_to_live=-1):
        super().__init__(x, y, current_frame, frame_added, frames_to_live)
        self.width = width
        self.height = height
        self.image = image

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        if isinstance(image, str):
            self.__image = Image.open(image).convert('RGBA').resize((self.width, self.height))
        elif type(image) is Image.Image:
            self.__image = image.convert('RGBA').resize((self.width, self.height))

    def render(self, image):
        self.apply_effects()
        image.paste(self.image, (self.x, self.y), mask=self.image)
