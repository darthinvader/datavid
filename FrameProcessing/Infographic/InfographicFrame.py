from PIL import Image
import bisect

class InfographicFrame:
    def __init__(self, mode='RGBA', width=3840, height=2160, color=(0, 0, 0, 0)):
        self.mode = mode
        self.width = width
        self.height = height
        self.image = Image.new(mode, (width, height), color)
        self.frame_items = list()
        self.info_items = list()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    @property
    def frame_items(self):
        return self.__frame_items

    @frame_items.setter
    def frame_items(self, frame_items):
        self.__frame_items = frame_items

    @property
    def info_items(self):
        return self.__info_items

    @info_items.setter
    def info_items(self, info_items):
        self.__info_items = info_items

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = mode

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

    def add_frame_item(self, frame_item):
        bisect.insort(self.frame_items, frame_item)

    def remove_frame_item(self, ID):
        for fi in self.__frame_items:
            if id(fi) == ID:
                self.__frame_items.remove(fi)

    def add_info_item(self, info_item):
        bisect.insort(self.info_items, info_item)

    def remove_info_item(self, ID):
        for fi in self.__frame_items:
            if id(fi) == ID:
                self.__info_items.remove(fi)

    # Define the rendering (which is the most difficult part)
    def render(self):
        pass

    def show(self):
        self.image.show()
