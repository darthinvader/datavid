class MapView:
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height
        self.items = list()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

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

    def add_to_list(self, item):
        self.items.append(item)

    def remove_from_list(self, item):
        self.items.remove(item)

    def render(self, image): pass
