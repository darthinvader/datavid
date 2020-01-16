from datavid import HelperFunctions
from datavid.BasicFrameItems.ShapeFrameItem import ShapeFrameItem
import math


class MapViewManager:
    def __init__(self, map_image, data=None, number_of_split_frames=10):
        self.map_image = map_image
        self.data = data
        self.data_chunks = None
        self.data_index = 0
        self.chunk_index = 0
        self.shapes = list()
        self.current_frame = 0
        self.number_of_split_frames = number_of_split_frames

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
        self.render_map(image)
        self.render_shapes(image)

    def check_and_split_data(self):
        if self.chunk_index == 0:
            self.data_chunks = HelperFunctions.split_data(self.data[self.data_index], self.frame_timer)
            self.data_index += 1

    def data_points_to_shapes(self):
        chunk = self.data_chunks[self.chunk_index]
        for data_point in chunk:
            percentage = data_point['percentage']
            map_area_square_rooted = math.sqrt(self.map_image.width * self.map_image.width)
            size = math.floor(percentage * map_area_square_rooted)
            width = size
            height = size
            x = self.get_x(data_point)
            y = self.get_y(data_point)

            shape_type = data_point['shape_type']
            fill_color = self.get_fill_color(data_point)
            outline_fill = self.get_outline_fill(data_point)
            outline_width = self.get_outline_width(data_point)
            frames_to_live = data_point['frames_to_live']

            shape_item = ShapeFrameItem(width, height, x, y, self.current_frame, None, shape_type, fill_color,
                                        outline_fill, outline_width, frames_to_live)
            self.set_shape_effects(data_point, shape_item)

            self.shapes.append(shape_item)

    def get_y(self, data_point):
        if 'latitude' in data_point.keys():
            latitude = data_point['latitude']
            width = self.map_image.width
            y = HelperFunctions.longitude_to_point(latitude, width)
        else:
            y = data_point['y']
        return y

    def get_x(self, data_point):
        if 'longitude' in data_point.keys():
            height = self.map_image.height
            longitude = data_point['longitude']
            x = HelperFunctions.longitude_to_point(longitude, height)
        else:
            x = data_point['x']
        return x

    def set_shape_effects(self, data_point, shape_item):
        if 'effects' in data_point.keys():
            effects = data_point['effects']
            if isinstance(effects, list):
                shape_item.add_effects_list(effects)
            else:
                shape_item.add_effect(effects)

    def get_outline_width(self, data_point):
        if 'outline_width' in data_point.keys():
            outline_width = data_point['outline_width']
        else:
            outline_width = 0
        return outline_width

    def get_outline_fill(self, data_point):
        if 'outline_fill' in data_point.keys():
            outline_fill = data_point['outline_fill']
        else:
            outline_fill = None
        return outline_fill

    def get_fill_color(self, data_point):
        if 'fill_color' in data_point.keys():
            fill_color = data_point['fill_color']
        else:
            fill_color = (255, 255, 255, 255)
        return fill_color

    def increment_chunk(self):
        self.chunk_index += 1
        if self.chunk_index >= self.number_of_split_frames:
            self.chunk_index = 0

    def render_map(self, image):
        self.map_image.render(image)

    def render_shapes(self, image):
        for shape in self.shapes:
            shape.render(image)
        self.increase_frame_counter()

    def increase_frame_counter(self):
        for shape in self.shapes:
            shape.increment_current_frame()
        filtered_list = filter(MapViewManager.item_expired, self.shapes)
        self.shapes = list(filtered_list)

    @staticmethod
    def item_expired(item):
        if item.is_dead():
            return False
        return True
