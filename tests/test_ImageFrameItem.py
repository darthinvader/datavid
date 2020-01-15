import unittest
from PIL import Image
from datavid.BasicFrameItems.ImageFrameItem import ImageFrameItem


class TestImageFrameItem(unittest.TestCase):
    def test_default_x(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img)
        self.assertEqual(ifi.x, 0)

    def test_default_y(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img)
        self.assertEqual(ifi.y, 0)

    def test_default_width(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img)
        self.assertEqual(ifi.width, 3840)

    def test_default_height(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img)
        self.assertEqual(ifi.height, 2080)

    def test_default_current_frame(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img)
        self.assertEqual(ifi.current_frame, 0)

    def test_default_frame_added(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img)
        self.assertEqual(ifi.frame_added, 0)

    def test_default_frames_to_live(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img)
        self.assertEqual(ifi.frames_to_live, -1)

    def test_current_frame_increment(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img, current_frame=10)
        ifi.increment_current_frame()
        self.assertEqual(ifi.current_frame, 11)

    def test_x(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img, x=5)
        self.assertEqual(ifi.x, 5)

    def test_y(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img, y=5)
        self.assertEqual(ifi.y, 5)

    def test_width(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img, width=5)
        self.assertEqual(ifi.width, 5)

    def test_height(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img, height=5)
        self.assertEqual(ifi.height, 5)

    def test_current_frame(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img, current_frame=5)
        self.assertEqual(ifi.current_frame, 5)

    def test_frame_added(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img, frame_added=5)
        self.assertEqual(ifi.frame_added, 5)

    def test_frames_to_live(self):
        img = Image.new("RGBA", (1920, 1080))
        ifi = ImageFrameItem(img,frames_to_live=10)
        self.assertEqual(ifi.frames_to_live, 10)
