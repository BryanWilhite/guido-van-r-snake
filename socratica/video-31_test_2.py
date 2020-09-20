import unittest

from math import pi
video_31 = __import__('video-31') # see https://stackoverflow.com/q/8350853/22944

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(video_31.area(1), pi)
        self.assertAlmostEqual(video_31.area(0), 0)
        self.assertAlmostEqual(video_31.area(2.1), pi * 2.1**2)

    def test_values(self):
        self.assertRaises(ValueError, video_31.area, -2)
