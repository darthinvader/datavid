from PIL import Image


class MapView:
    def __init__(self, image_path, width, height, x=0, y=0):
        self.image = image_path
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.items = list()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image_path):
        self.__image = Image.open(image_path).convert('RGBA').resize((self.width, self.height))

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

    def add_to_list(self, item):
        self.items.append(item)

    def remove_from_list(self, item):
        self.items.remove(item)

    def tick_down_items(self):
        for item in self.items:
            item.tick_down()
        self.items = filter(MapView.item_ticks_zeroed, self.items)

    @staticmethod
    def item_ticks_zeroed(item):
        if item.ticks <= 0:
            return False
        return True

    def render(self, image):
        image.paste(self.image, (self.x, self.y), mask=self.image)
        for item in self.items:
            item.shape_item.render(image)
        self.tick_down_items()
