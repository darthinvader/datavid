from FrameProcessing.FrameItem import FrameItem


class TextItem(FrameItem):
    def __init__(self, text, width, height, x=0, y=0, order=1, lines_amount=1):
        super().__init__(width, height, x, y, order)
        self.text = text
        self.lines_amount = lines_amount

    def get_text(self):
        """
        This function returns the text.
        :param self:
        :return: the map image
        """
        return self.text

    def set_text(self, text):
        """
        This function sets the text.
        :param text: the text to be set.
        """
        self.text = text

    def get_lines_amount(self):
        """
        This function returns the amount of lines of the TextItem.
        :return: the amount of lines of the TextItem.
        """
        return self.lines_amount

    def set_lines_amount(self, lines_amount):
        """
        Sets the amount of lines of the TextItem.
        :param lines_amount: the amount of lines of the TextItem.
        """
        self.lines_amount = lines_amount

    def render(self, image):
        pass