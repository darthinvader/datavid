import unittest
from PIL import Image
from datavid.BasicFrameItems.ShapeFrameItem import ShapeFrameItem


class TestTextFrameItem(unittest.TestCase):
    def test_default_x(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.x, 0)

    def test_default_y(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.y, 0)

    def test_default_width(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.width, 0)

    def test_default_height(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.height, 0)

    def test_default_current_frame(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.current_frame, 0)

    def test_default_frame_addded(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.frame_added, 0)

    def test_default_fill_color(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.fill_color, (255,255,255,255))

    def test_default_outline_fill(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.outline_fill, None)

    def test_default_outline_width(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.outline_width, 0)

    def test_default_frames_to_live(self):
        sfi = ShapeFrameItem()
        self.assertEqual(sfi.frames_to_live, -1)

    def test_current_frame_increment(self):
        sfi = ShapeFrameItem(current_frame=10)
        sfi.increment_current_frame()
        self.assertEqual(sfi.current_frame, 11)

    def test_x(self):
        sfi = ShapeFrameItem(x=5)
        self.assertEqual(sfi.x, 5)

    def test_y(self):
        sfi = ShapeFrameItem(y=5)
        self.assertEqual(sfi.y, 5)

    def test_current_frame(self):
        sfi = ShapeFrameItem(current_frame=5)
        self.assertEqual(sfi.current_frame, 5)

    def test_frame_added(self):
        sfi = ShapeFrameItem(frame_added=5)
        self.assertEqual(sfi.frame_added, 5)

    def test_shape_type(self):
        sfi = ShapeFrameItem(shape_type="Box")
        self.assertEqual(sfi.shape_type, "Box")

    def test_fill_color(self):
        sfi = ShapeFrameItem(fill_color=(255,255,255,0))
        self.assertEqual(sfi.fill_color, (255,255,255,0))

    def test_outline_fill(self):
        sfi = ShapeFrameItem(outline_fill=(255,255,255,0))
        self.assertEqual(sfi.outline_fill, (255,255,255,0))

    def test_outline_width(self):
        sfi = ShapeFrameItem(outline_width=5)
        self.assertEqual(sfi.outline_width, 5)

    def test_frames_to_live(self):
        sfi = ShapeFrameItem(frames_to_live=10)
        self.assertEqual(sfi.frames_to_live, 10)
