class MapShapeFactory:
    def __init__(self, map_view, width=10, height=10, shape_type="Ellipse", fill_color=(255, 0, 0, 255),
                 outline_fill=(255, 0, 0, 255), outline_width=0, ticks=60, frame_timer=10):
        self.map_view = map_view
        self.width = width
        self.height = height
        self.shape_type = shape_type
        self.fill_color = fill_color
        self.outline_fill = outline_fill
        self.outline_width = outline_width
        self.ticks = ticks
        self.frame_timer = frame_timer

    @property
    def map_view(self):
        return self.__map_view

    @map_view.setter
    def map_view(self, map_view):
        self.__map_view = map_view

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

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

    @property
    def ticks(self):
        return self.__ticks

    @ticks.setter
    def ticks(self, ticks):
        self.__ticks = ticks

    @property
    def frame_timer(self):
        return self.__frame_timer

    @frame_timer.setter
    def frame_timer(self, frame_timer):
        self.__frame_timer = frame_timer
