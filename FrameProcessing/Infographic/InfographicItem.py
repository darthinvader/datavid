class InfographicItem:

    def __init__(self, main_info_number, bar):
        """
        :param main_info_number: the number that describes how big the bar should be
        :param bar: the bar which is a shapeItem
        """
        self.main_info_number = main_info_number
        self.bar = bar

    @property
    def main_info_number(self):
        return self.__main_info_number

    @main_info_number.setter
    def main_info_number(self, main_info_number):
        self.__main_info_number = main_info_number

    @property
    def bar(self):
        return self.__bar

    @bar.setter
    def bar(self, bar):
        self.__bar = bar

    def render(self, image):
        pass
