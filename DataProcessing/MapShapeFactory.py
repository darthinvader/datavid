from PIL import Image
from FrameProcessing.MapView.MapShapeItem import MapShapeItem
from FrameProcessing.BasicItems.ShapeItem import ShapeItem
from DataProcessing import DataframeProcess
import math


class MapShapeFactory:
    def __init__(self, map_view, data=None, frame_timer=10):
        self.map_view = map_view
        self.data = data
        # the data contain all the settings of the shape_item. Those are:
        # shape type, fill color, outline color, outline width as well as the ticks it will live for.
        self.frame_timer = frame_timer
        self.data_chunks = None
        self.data_index = 0
        self.chunk_index = 0

    @property
    def map_view(self):
        return self.__map_view

    @map_view.setter
    def map_view(self, map_view):
        self.__map_view = map_view

    @property
    def frame_timer(self):
        return self.__frame_timer

    @frame_timer.setter
    def frame_timer(self, frame_timer):
        self.__frame_timer = frame_timer

    @property
    def data_index(self):
        return self.__data_index

    @data_index.setter
    def data_index(self, data_index):
        self.__data_index = data_index

    @property
    def chunk_index(self):
        return self.__chunk_index

    @chunk_index.setter
    def chunk_index(self, chunk_index):
        self.__chunk_index = chunk_index

    @property
    def data_chunks(self):
        return self.__data_chunks

    @data_chunks.setter
    def data_chunks(self, data_chunks):
        self.__data_chunks = data_chunks

    def render_next_frame(self, image):
        if self.data_index >= len(self.data):
            return True

        if self.chunk_index == 0:
            self.data_chunks = DataframeProcess.split_data(self.data[self.data_index], self.frame_timer)
            self.data_index += 1
        chunk = self.data_chunks[self.chunk_index]

        for data_point in chunk:
            size = math.floor(data_point['percentage'] * math.sqrt(self.map_view.width * self.map_view.width))
            x = data_point['x']
            y = data_point['y']
            shape_type = data_point['shape_type']
            fill_color = data_point['fill_color']
            outline_fill = data_point['outline_fill']
            outline_width = data_point['outline_width']
            ticks = data_point['ticks']
            width = size
            height = size

            shape_item = ShapeItem(width, height, shape_type, x, y, fill_color, outline_fill, outline_width)
            map_shape_item = MapShapeItem(shape_item, ticks)
            self.map_view.add_item(map_shape_item)

        self.chunk_index += 1
        if self.chunk_index >= self.frame_timer:
            self.chunk_index = 0

        self.map_view.render(image)
        return False
