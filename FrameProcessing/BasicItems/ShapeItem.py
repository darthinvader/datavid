import math

from PIL import ImageDraw, Image

from FrameProcessing.BasicItems.FrameItem import FrameItem


class ShapeItem(FrameItem):
    def __init__(self, width=0, height=0, shape_type="Ellipse", x=0, y=0, fill_color=(255, 255, 255, 255),
                 outline_fill=None, outline_width=0):
        super().__init__(width, height, x, y)
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

    @property
    def outline_fill(self):
        return self.__outline_fill

    @outline_fill.setter
    def outline_fill(self, outline_fill):
        self.__outline_fill = outline_fill

    @property
    def outline_width(self):
        return self.__outline_width

    @outline_width.setter
    def outline_width(self, outline_width):
        self.__outline_width = outline_width

    def render(self, image):
        shape_layer_position = (math.floor(self.x - self.width / 2), math.floor(self.y - self.height / 2))
        bounding_box = (
            0, 0, self.width, self.height)

        # Firstly we create a shape_layer and draw the shape in it
        shape_layer = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(shape_layer, 'RGBA')
        # Then we check what type of shape is the shape
        if self.shape_type == "Ellipse":
            draw.ellipse(bounding_box, fill=self.fill_color, outline=self.outline_fill, width=self.outline_width)
        elif self.shape_type == "Box":
            draw.rectangle(bounding_box, fill=self.fill_color, outline=self.outline_fill, width=self.outline_width)

        # and then we paste the shape_layer into the image
        image.paste(shape_layer, shape_layer_position, shape_layer)
