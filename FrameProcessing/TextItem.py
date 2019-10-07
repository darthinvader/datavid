from FrameProcessing.FrameItem import FrameItem


class TextItem(FrameItem):
    def __init__(self, text, width, height, x=0, y=0, order=1, lines_amount=1):
        super().__init__(width, height, x, y, order)
        self.text = text
        self.lines_amount = lines_amount

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def lines_amount(self):
        return self.__lines_amount

    @lines_amount.setter
    def lines_amount(self, lines_amount):
        self.__lines_amount = lines_amount

    def render(self, image):
        pass