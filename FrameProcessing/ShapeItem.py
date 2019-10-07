from FrameProcessing.FrameItem import FrameItem
from PIL import ImageDraw


class ShapeItem(FrameItem):

    def __init__(self, shape_type, width, height, x=0, y=0, order=1, fill_color=(255, 0, 0, 255),
                 outline_fill=(255, 0, 0, 255), outline_width=0):
        super().__init__(width, height, x, y, order)
        self.shape_type = shape_type
        self.fill_color = fill_color
        self.outline_fill = outline_fill
        self.outline_width = outline_width

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
        bounding_box = (
            self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2)
        draw = ImageDraw.Draw(image, 'RGBA')
        if self.shape_type == "Ellipse":
            draw.ellipse(bounding_box, fill=self.fill_color, outline=self.outline_fill, width=self.outline_width)
        elif self.shape_type == "Box":
            draw.rectangle(bounding_box, fill=self.fill_color, outline=self.outline_fill, width=self.outline_width)