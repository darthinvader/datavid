from PIL import ImageFont, Image, ImageDraw

from datavid.BasicFrameItems.AbstractFrameItem import AbstractFrameItem


# Direction on text doesn't work right now!

class TextFrameItem(AbstractFrameItem):
    def __init__(self, font_path, text="", x=0, y=0, current_frame=0, frame_added=None, font_size=10,
                 fill_color=(255, 255, 255, 255), spacing=0, align="center", direction="ltr", frames_to_live=-1):
        super().__init__(x, y, current_frame, frame_added, frames_to_live)
        self.text = text
        self.font_size = font_size
        if font_path[-3:] == 'ttf':
            self.font = ImageFont.truetype(font_path, self.font_size)
        elif font_path[-3:] == 'otf':
            self.font = ImageFont.FreeTypeFont(font_path, self.font_size)
        self.fill_color = fill_color
        self.spacing = spacing
        self.align = align
        self.direction = direction

    def render(self, image):
        self.apply_effects()
        # We create a new text layer image and since we don't know how big the text is going to be we just
        # assign it the size of the image we are going to paste the text and we make it all transparent
        text_layer = Image.new("RGBA", (image.width, image.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer, 'RGBA')
        # Then we draw the text onto the the text layer
        draw.text((self.x, self.y), self.text, self.fill_color, self.font, spacing=self.spacing, align=self.align)
        # And then we paste the text layer on our image
        image.paste(text_layer, (0, 0), text_layer)
