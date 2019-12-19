class ShapeEffectsManager:
    def __init__(self, effects, shape):
        self.effects = effects
        self.frame_counter = 0
        self.shape = shape

    @property
    def effects(self):
        return self.__effects

    @effects.setter
    def effects(self, effects):
        self.__effects = effects

    def add_effect(self, effect):
        self.effects.append(effect)

    @property
    def frame_counter(self):
        return self.__frame_counter

    @frame_counter.setter
    def frame_counter(self, frame_counter):
        self.__frame_counter = frame_counter

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape):
        self.__shape = shape

    def initialize_shape_effects(self):
        for effect in self.effects:
            effect.add_shape(self.shape)

    def tick_frame(self):
        self.frame_counter += 1
        for effect in self.effects:
            effect.apply_effect(self.frame_counter)
