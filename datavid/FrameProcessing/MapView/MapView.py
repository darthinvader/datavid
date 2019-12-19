from PIL import Image


class MapView:
    def __init__(self, image_path, width=3840, height=2160, x=0, y=0):
        self.width = width
        self.height = height
        self.image = image_path
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

    def add_item(self, item):
        self.items.append(item)

    def add_items(self, items):
        self.items.extend(items)

    def remove_item(self, item):
        self.items.remove(item)

    def tick_down(self):
        """
            Ticks down the items and then removes the ones that are less than 0
        """
        for item in self.items:
            item.tick_down()
        filtered_list = filter(MapView.item_ticks_zeroed, self.items)
        self.items = list(filtered_list)

    @staticmethod
    def item_ticks_zeroed(item):
        if item.ticks <= 0:
            return False
        return True

    def render(self, image):
        """
            Renders the current map with the current items.
        """
        # First we paste our Map Image into the image
        image.paste(self.image, (self.x, self.y), mask=self.image)

        # Then we render every item we have into the image
        for item in self.items:
            item.render(image)

        # Then we tick down the items
        self.tick_down()
