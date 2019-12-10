from PIL import Image
from FrameProcessing.MapView.MapShapeItem import MapShapeItem
from FrameProcessing.BasicItems.ShapeItem import ShapeItem
import math


class MapShapeFactory:
    def __init__(self, map_view, data=None, width=3840, height=2160, shape_type="Ellipse", fill_color=(255, 0, 0, 255),
                 outline_fill=(255, 0, 0, 255), outline_width=0, ticks=60, frame_timer=10):
        self.map_view = map_view
        self.data = data
        # the data contain the position of the shape as well
        # as the time it appears and the size of the shape (via percentage of the size of the image)
        self.width = width
        self.height = height
        self.shape_type = shape_type
        self.fill_color = fill_color
        self.outline_fill = outline_fill
        self.outline_width = outline_width
        self.ticks = ticks
        self.frame_timer = frame_timer
        self.frames = list()

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

    @property
    def frames(self):
        return self.__frames

    @frames.setter
    def frames(self, frames):
        self.__frames = frames

    def add_frame(self, frame):
        self.frames.append(frame)

    def run_renders(self):
        for current_data in self.data:
            self.add_data_to_view_map(current_data)

    def add_data_to_view_map(self, data):
        chunks = MapShapeFactory.split_data(data, self.frame_timer)
        for chunk in chunks:
            frame = Image.new('RGBA', (self.width, self.height), (255, 255, 255, 255))
            for data in chunk:
                size = math.floor(data['percentage'] * math.sqrt(self.width * self.height))
                x = data['x']
                y = data['y']
                width = size
                height = size

                shape_item = ShapeItem(width, height, self.shape_type, x, y, self.fill_color, self.outline_fill,
                                       self.outline_width)
                map_shape_item = MapShapeItem(shape_item, self.ticks)
                self.map_view.add_item(map_shape_item)
            self.map_view.render(frame)
            self.add_frame(frame)

    @staticmethod
    def split_data(data_list, pieces):
        data_list_length = len(data_list)
        chunk_length = math.floor(len(data_list) / pieces)
        chunks = [data_list[x:x + chunk_length] for x in range(0, data_list_length, chunk_length)]
        if chunk_length * pieces < data_list_length:
            chunks[-2].extend(chunks[-1])
            chunks = chunks[1:-2]
        return chunks

    @staticmethod
    def longitude_to_point(longitude, image_width):
        return math.ceil((image_width / 360) * (180 + longitude))

    @staticmethod
    def latitude_to_point(latitude, image_height):
        return math.ceil((image_height / 180) * (90 - latitude))
