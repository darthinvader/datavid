import math

from PIL import ImageDraw, Image

from datavid.BasicFrameItems.AbstractFrameItem import AbstractFrameItem


class ShapeFrameItem(AbstractFrameItem):
    def __init__(self, width=0, height=0, x=0, y=0, current_frame=0, frame_added=None, shape_type='Ellipse',
                 fill_color=(255, 255, 255, 255), outline_fill=None, outline_width=0, frames_to_live=-1):
        super().__init__(x, y, current_frame, frame_added, frames_to_live)
        self.width = width
        self.height = height
        self.shape_type = shape_type
        self.fill_color = fill_color
        self.outline_fill = outline_fill
        self.outline_width = outline_width

    def render(self, image):
        self.apply_effects()
        shape_layer_position = (math.floor(self.x - self.width / 2), math.floor(self.y - self.height / 2))
        bounding_box = (0, 0, self.width, self.height)

        # Firstly we create a shape_layer and draw the shape in it
        shape_layer = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(shape_layer, 'RGBA')
        # Then we check what type of shape is the shape
        if self.shape_type == "Ellipse":
            draw.ellipse(bounding_box, fill=self.fill_color, outline=self.outline_fill, width=self.outline_width)
        elif self.shape_type == "Box":
            draw.rectangle(bounding_box, fill=self.fill_color, outline=self.outline_fill, width=self.outline_width)

        # and then we paste the shape_layer into the image
        image.paste(shape_layer, shape_layer_position, shape_layer)
