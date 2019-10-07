from FrameProcessing.ImageItem import ImageItem
from FrameProcessing.Map.MapFrameItem import MapFrameItem


class MapFrame(ImageItem):

    def __init__(self, image_path, width, height, x=0, y=0, order=1):
        super().__init__(image_path, width, height, x, y, order)

    def decay_frame_items(self):
        for fi in self.frame_items:
            if type(fi) == MapFrameItem:
                fi.decay()

    def remove_decayed_items(self):
        for fi in self.frame_items:
            if type(fi) == MapFrameItem:
                if fi.decay == 0:
                    self.remove_frame_item(id(fi))

    def render(self, image):
        self.remove_decayed_items()
        super().render(image)
        self.decay_frame_items()
