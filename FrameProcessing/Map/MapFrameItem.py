from FrameProcessing.ShapeItem import ShapeItem
import math


class MapFrameItem(ShapeItem):
    def __init__(self, longitude, latitude, order=1, fill_color=(255, 0, 0, 255), decay_timer=1, percentage=0.001):
        super().__init__(0, 0, 0, 0, order, fill_color)
        self.percentage = percentage
        self.longitude = longitude
        self.latitude = latitude
        self.decay_timer = decay_timer

    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage):
        if percentage > 1:
            percentage = 1
        elif percentage < 0:
            percentage = 0
        self.__percentage = percentage

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        if longitude > 180:
            longitude = 180
        elif longitude < -180:
            longitude = -180
        self.__longitude = longitude

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

    @property
    def decay_timer(self):
        return self.__decay_timer

    @decay_timer.setter
    def decay_timer(self, decay_timer):
        self.__decay_timer = decay_timer

    def decay(self):
        self.decay_timer -= 1

    def calculate_position(self, image_width, image_height):
        self.x = math.floor((image_width / 360) * (180 + self.longitude))
        self.y = math.floor((image_height / 360) * (90 - self.latitude))

    def calculate_size(self, image_width, image_height):
        self.width = ((image_width * image_height) * (self.percentage ** 2)) / 2
        self.height = self.width

    def render(self, image):
        self.calculate_position(image.width, image.height)
        self.calculate_size(image.width, image.height)
        super().render(image)
