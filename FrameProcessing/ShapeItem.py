from FrameProcessing.FrameItem import FrameItem


class ShapeItem(FrameItem):
    def __init__(self, shape_type, width, height, x=0, y=0, fill_color=(255, 0, 0, 255),
                 outline_fill=(255, 0, 0, 255), outline_width=0):
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
        pass
