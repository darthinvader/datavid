class MapShapeManager:
    def __init__(self, shape_item, ticks=100, effect_manager=None):
        self.shape_item = shape_item
        self.ticks = ticks
        self.effect_manager = effect_manager

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

    @property
    def effect_manager(self):
        return self.__effect_manager

    @effect_manager.setter
    def effect_manager(self, effect_manager):
        self.__effect_manager = effect_manager

    def tick_down(self):
        if self.effect_manager is not None:
            self.effect_manager.tick_frame()
        self.ticks -= 1

    def render(self, image):
        self.shape_item.render(image)
