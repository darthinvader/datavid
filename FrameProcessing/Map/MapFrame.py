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
        decayed_items_id = list()
        for fi in self.frame_items:
            if type(fi) == MapFrameItem:
                if fi.decay_timer == 0:
                    decayed_items_id.append(id(fi))

        for did in decayed_items_id:
            self.remove_frame_item(did)

    def render(self, image):
        self.remove_decayed_items()
        super().render(image)
        self.decay_frame_items()
