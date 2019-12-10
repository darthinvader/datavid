class MapShapeItem:
    def __init__(self, shape_item, ticks):
        self.shape_item = shape_item
        self.ticks = ticks

    @property
    def shape_item(self):
        return self.__shape_item

    @shape_item.setter
    def shape_item(self, shape_item):
        self.__shape_item = shape_item

    @property
    def ticks(self):
        return self.__ticks

    @ticks.setter
    def ticks(self, ticks):
        self.__ticks = ticks

    def tick_down(self):
        self.ticks -= 1
