from PIL import Image, ImageDraw
import math


class WorldMapFrame:

    def __init__(self, photo_path):
        """
        This is the initialization function of the WorldMapFrame.
        This function loads the world_image and sets the local variables width = image width
        height = image height
        and x and y variables to 0.
        :param self: The WorldMapFrame.
        :param photo_path: the path of the world map.
        :return: nothing
        """
        self.world_image = Image.open(photo_path).convert('RGBA')
        self.resized_world_image = None
        self.map_width = self.world_image.width
        self.map_height = self.world_image.height
        self.x = 0
        self.y = 0

    def get_image(self):
        """
        This function returns the map image.
        :param self:
        :return: the map image
        """
        return self.world_image

    def get_width(self):
        """
        This function returns the map's width
        :param self:
        :return: returns the map's width
        """
        return self.map_width

    def get_height(self):
        """
        This fnction returns the map's height
        :param self:
        :return: returns the map's height
        """
        return self.map_height

    def get_x(self):
        """
        This function returns the map's x position.
        :param self:
        :return: the map's x position.
        """
        return self.x

    def get_y(self):
        """
        This function returns the map's y position.
        :param self:
        :return: the map's y position.
        """
        return self.y

    def set_width(self, width):
        """
        This function sets the map's width.
        :param self:
        :param width: the new width of the map
        :return: None.
        """
        self.map_width = width

    def set_height(self, height):
        """
         This function sets the map's height.
         :param self:
         :param height: the new height of the map
         :return: None
         """
        self.map_height = height

    def set_x(self, x):
        """
        Sets the map's x position.
        :param x: the map's x position.
        :return: None
        """
        self.x = x

    def set_y(self, y):
        """
        Sets the map's y position.
        :param y: the map's y position.
        :return: None
        """
        self.y = y

    def add_to_image(self, image, x=None, y=None, width=None, height=None):
        """
        Adds the world map image to the x,y coordinate of the image with width equal
        to width and height equal to height. The it assigns x, y, width, height to the map's variables.
        :param self:
        :param image: The image we are going to paste the wold map to.
        :param x: the x coordinate position in the image we want to paste the world map
        :param y: the y coordinate position in the image we want to paste the world map
        :param width: the width of the world map
        :param height: the height of the world map
        :return: None
        """
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        if width is None:
            width = self.map_width
        if height is None:
            height = self.map_height
        # The following check is for performance reasons. If the world_image is not going to be resized
        # so we are going to save a good percentage of time (from testing 30% - 40%)
        if self.resized_world_image is None:
            self.resized_world_image = self.world_image.resize((width, height))
        elif not (height == self.resized_world_image.height and width == self.resized_world_image.width):
            self.resized_world_image = self.world_image.resize((width, height))

        image.paste(self.resized_world_image, (x, y), self.resized_world_image)
        self.x = x
        self.y = y
        self.map_width = width
        self.map_height = height

    def add_circle_to_map(self, image, latitude, longitude, percentage_size=0.001, fill_color=(255, 0, 0, 255)):
        """
        This function adds a circle in the latitude , longitude transformed to fit an equidistant world map.
        The percentage_size is used to make a square that is equal to the map's area multiplied by the percentage_size
        squared (makes a square that is the percentage size of the map in each dimension).
        For example if the size of the map is 100*200 and the percentage is 1%(0.01) then the size of the square is
        100*200 * (1%)^2 = 2 pixels in each dimension making 4 pixels square where the circle will fit in (which means)
        the diameter of the circle is 2 pixels.
        :param self:
        :param image: the image we are going to add the circle.
        :param latitude: the latitude of the circle
        :param longitude: the longitude of the circle
        :param percentage_size: the percentage size of the circle
        :param fill_color: the color of the circle
        :return: None
        """
        x = math.floor(self.x + (self.map_width / 360) * (180 + longitude))
        y = math.floor(self.y + (self.map_height / 180) * (90 - latitude))
        # I calculate the size of the circle based of the
        # the area of the map times the percentage size squared
        size = math.floor(((self.map_width * self.map_height) * (percentage_size ** 2)) / 2)
        circle_box = (x - size, y - size, x + size, y + size)
        draw = ImageDraw.Draw(image, 'RGBA')
        draw.ellipse(circle_box, fill=fill_color)

    def add_multiple_circles_to_map(self, image, latitudes, longitudes, percentage_size=0.001,
                                    fill_color=(255, 0, 0, 255)):
        """
        This function adds circles in the latitudes , longitudes transformed to fit an equidistant world map.
        The percentage_size is used to make a square that is equal to the map's area multiplied by the percentage_size
        squared (makes a square that is the percentage size of the map in each dimension).
        For example if the size of the map is 100*200 and the percentage is 1%(0.01) then the size of the square is
        100*200 * (1%)^2 = 2 pixels in each dimension making 4 pixels square where the circle will fit in (which means)
        the diameter of the circle is 2 pixels.
         :param self:
        :param image: the image we are going to add the circle.
        :param latitudes: the latitudes of the circles
        :param longitudes: the longitudes of the circles
        :param percentage_size: the percentage size of the circle
        :param fill_color: the color of the circle
        :return: None
        """
        for i in range(0, len(latitudes)):
            self.add_circle_to_map(image, latitudes[i], longitudes[i], percentage_size, fill_color)
