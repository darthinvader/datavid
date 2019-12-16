from FrameProcessing.MapView.MapShapeItem import MapShapeItem
from FrameProcessing.BasicItems.ShapeItem import ShapeItem
from DataProcessing import DataframeProcess
import math


class MapShapeFactory:
    def __init__(self, map_view, data=None, frame_timer=10):
        self.map_view = map_view
        # the data contain all the settings of the shape_item. Those are:
        # shape type, fill color, outline color, outline width, effects as well as the ticks it will live for.
        self.data = data
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
        """
            Allocates the data on the map accordingly then render the map on top of the image.
            @param image: the image we are going to render on top of
            @return: Whether the render run correctly or not
        """
        # First we check if we are finished with our data and if we are we return False
        if self.data_index >= len(self.data):
            return False

        # Then we check if we are at the start of the data so we chop it into chunks
        self.check_and_split_data()

        # The chunks are created in order to fill the in-between frames of the video with something so
        # that they are not still images repeating

        # Then we create new shapes for each data point to append to the map
        self.data_points_to_shapes()

        # we increment the chunk we are in
        self.increment_chunk()

        # then render the map view
        self.map_view.render(image)

        # If the render was successful we return True
        return True

    def data_points_to_shapes(self):
        """
            Assigns to the map our data_points as shapes.
        """
        # We take our chunk
        chunk = self.data_chunks[self.chunk_index]
        for data_point in chunk:
            # Then we collect our x,y,shape_type,fill_color,outline_fill,outline_width,ticks,effects,width,height
            # So we can assign them to our shapeItem
            x = data_point['x']
            y = data_point['y']
            shape_type = data_point['shape_type']
            fill_color = data_point['fill_color']
            outline_fill = data_point['outline_fill']
            outline_width = data_point['outline_width']
            ticks = data_point['ticks']
            effects = data_point['effects']  # As of now they are not used

            # percentage is a number between 1 and 0 that makes the shape have area equal to the percentage of the map
            size = math.floor(data_point['percentage'] * math.sqrt(self.map_view.width * self.map_view.width))
            width = size
            height = size

            # We create our shape
            shape_item = ShapeItem(width, height, shape_type, x, y, fill_color, outline_fill, outline_width)
            map_shape_item = MapShapeItem(shape_item, ticks)

            # we add our shapes to the MapView
            self.map_view.add_item(map_shape_item)

    def increment_chunk(self):
        self.chunk_index += 1
        if self.chunk_index >= self.frame_timer:
            self.chunk_index = 0

    def check_and_split_data(self):
        if self.chunk_index == 0:
            self.data_chunks = DataframeProcess.split_data(self.data[self.data_index], self.frame_timer)
            self.data_index += 1
