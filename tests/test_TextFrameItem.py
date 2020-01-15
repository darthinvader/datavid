import unittest
from PIL import Image
from datavid.BasicFrameItems.TextFrameItem import TextFrameItem


class TestTextFrameItem(unittest.TestCase):
    def test_default_x(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.x, 0)

    def test_default_y(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.y, 0)

    def test_default_current_frame(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.current_frame, 0)

    def test_default_frame_addded(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.frame_added, 0)

    def test_default_font_size(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.font_size, 10)

    def test_default_fill_color(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.fill_color, (255,255,255,255))

    def test_default_spacing(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.spacing, 0)

    def test_default_align(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.align, "center")

    def test_default_direction(self):
        tfi = TextFrameItem("", "")
        self.assertEqual(tfi.direction, "ltr")

    def test_default_frames_to_live(self):
        tfi = TextFrameItem("","")
        self.assertEqual(tfi.frames_to_live, -1)

    def test_current_frame_increment(self):
        tfi = TextFrameItem("", "",current_frame=10)
        tfi.increment_current_frame()
        self.assertEqual(tfi.current_frame, 11)

    def test_x(self):
        tfi = TextFrameItem("", "",x=5)
        self.assertEqual(tfi.x, 5)

    def test_y(self):
        tfi = TextFrameItem("", "",y=5)
        self.assertEqual(tfi.y, 5)

    def test_current_frame(self):
        tfi = TextFrameItem("", "",current_frame=5)
        self.assertEqual(tfi.current_frame, 5)

    def test_frame_added(self):
        tfi = TextFrameItem("", "",frame_added=5)
        self.assertEqual(tfi.frame_added, 5)

    def test_font_size(self):
        tfi = TextFrameItem("", "", font_size=5)
        self.assertEqual(tfi.font_size, 5)

    def test_fill_color(self):
        tfi = TextFrameItem("", "", fill_color=(255,255,255,0))
        self.assertEqual(tfi.fill_color, (255,255,255,0))

    def test_spacing(self):
        tfi = TextFrameItem("", "", spacing=5)
        self.assertEqual(tfi.spacing, 5)

    def test_align(self):
        tfi = TextFrameItem("", "", align="right")
        self.assertEqual(tfi.align, "right")

    def test_direction(self):
        tfi = TextFrameItem("", "", direction="ltra")
        self.assertEqual(tfi.direction, "ltra")

    def test_frames_to_live(self):
        tfi = TextFrameItem("", "", frames_to_live=10)
        self.assertEqual(tfi.frames_to_live, 10)
