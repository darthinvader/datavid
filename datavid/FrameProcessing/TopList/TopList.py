from PIL import Image


class TopList:
    def __init__(self, image_path, width, height, x, y, amount_of_elements):
        self.image = image_path
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.amount_of_elements = amount_of_elements
        self.elements = list()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image_path):
        self.__image = Image.open(image_path).convert('RGBA').resize((self.width, self.height))

    def add_element(self, element):
        self.elements.append(element)

    def render(self, image):
        pass
