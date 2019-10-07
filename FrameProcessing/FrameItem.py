from abc import ABC, abstractmethod


class FrameItem(ABC):

    def __init__(self, width, height, x=0, y=0, angle=0, order=1):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.angle = angle
        self.order = order

    def __lt__(self, other):
        return self.order < other.order

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
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        self.__angle = angle

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    @abstractmethod
    def render(self, image): pass
