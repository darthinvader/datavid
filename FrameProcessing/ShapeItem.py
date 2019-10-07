from FrameProcessing.FrameItem import FrameItem
from PIL import ImageDraw


class ShapeItem(FrameItem):

    def __init__(self, shape_type, width, height, x=0, y=0, order=1, fill_color=(255, 0, 0, 255)):
        super().__init__(width, height, x, y, order)
        self.shape_type = shape_type
        self.fill_color = fill_color

    @property
    def shape_type(self):
        return self.__shape_type

    @shape_type.setter
    def shape_type(self, shape_type):
        self.__shape_type = shape_type

    @property
    def fill_color(self):
        return self.__fill_color

    @fill_color.setter
    def fill_color(self, fill_color):
        self.__fill_color = fill_color

    def render(self, image):
        if self.shape_type == "Ellipse":
            circle_box = (
            self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2)
            draw = ImageDraw.Draw(image, 'RGBA')
            draw.ellipse(circle_box, fill=self.fill_color)
