import unittest
from unittest.mock import MagicMock, call
from m5stack import lcd
import font16seg

class TestFont16seg(unittest.TestCase):
    def setUp(self):
        font16seg.resetAttributes()

    def test_attrib16seg(self):
        font16seg.attrib16seg(10, 8, lcd.BLUE, unlit_color=lcd.RED, letter_spacing=6, rotate=270)
        self.assertEqual(font16seg._length, 10)
        self.assertEqual(font16seg._width, 8)
        self.assertEqual(font16seg._color, lcd.BLUE)
        self.assertEqual(font16seg._unlit_color, lcd.RED)
        self.assertEqual(font16seg._letter_spacing, 6)
        self.assertEqual(font16seg._rotate, 270)

    def test_attrib16seg_too_small_length(self):
        font16seg.attrib16seg(2, 2, lcd.BLUE)
        self.assertEqual(font16seg._length, 3)
        self.assertEqual(font16seg._width, 2)
        self.assertEqual(font16seg._color, lcd.BLUE)

    def test_attrib16seg_too_small_width(self):
        font16seg.attrib16seg(3, 1, lcd.BLUE)
        self.assertEqual(font16seg._length, 3)
        self.assertEqual(font16seg._width, 2)
        self.assertEqual(font16seg._color, lcd.BLUE)

    def test_attrib16seg_width_must_not_bigger_than_length(self):
        font16seg.attrib16seg(10, 11, lcd.BLUE)
        self.assertEqual(font16seg._length, 10)
        self.assertEqual(font16seg._width, 10)
        self.assertEqual(font16seg._color, lcd.BLUE)

    def test_attrib16seg_reset_unlit_color(self):
        font16seg.attrib16seg(10, 8, lcd.BLUE, unlit_color=None)
        self.assertIsNone(font16seg._unlit_color)

    def test_attrib16seg_rotate_only_accepts_multiple_of_90(self):
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=270)
        self.assertEqual(font16seg._rotate, 270)
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=180)
        self.assertEqual(font16seg._rotate, 180)
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=90)
        self.assertEqual(font16seg._rotate, 90)
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=0)
        self.assertEqual(font16seg._rotate, 0)

        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=1)
        self.assertEqual(font16seg._rotate, 0)
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=360)
        self.assertEqual(font16seg._rotate, 0)
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=-90)
        self.assertEqual(font16seg._rotate, 0)
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=None)
        self.assertEqual(font16seg._rotate, 0)

    def test_resetAttributes(self):
        font16seg.attrib16seg(10, 8, lcd.BLUE, unlit_color=lcd.RED, letter_spacing=6, rotate=270)
        self.assertEqual(font16seg._length, 10)
        self.assertEqual(font16seg._width, 8)
        self.assertEqual(font16seg._color, lcd.BLUE)
        self.assertEqual(font16seg._unlit_color, lcd.RED)
        self.assertEqual(font16seg._letter_spacing, 6)
        self.assertEqual(font16seg._rotate, 270)

        font16seg.resetAttributes()
        self.assertEqual(font16seg._length, 8)
        self.assertEqual(font16seg._width, 2)
        self.assertEqual(font16seg._color, lcd.get_fg())
        self.assertIsNone(font16seg._unlit_color)
        self.assertEqual(font16seg._letter_spacing, 3)
        self.assertEqual(font16seg._rotate, 0)

    def test_text(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.text(0, 0, "0")
        self.assertEqual(lcd.triangle.call_count, 20)
        self.assertEqual(lcd.rect.call_count, 8)

    def test_text_with_unlit_color(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=lcd.DARKGREY)
        font16seg.text(0, 0, "0")
        self.assertEqual(lcd.triangle.call_count, 32)
        self.assertEqual(lcd.rect.call_count, 12)

    def test_text_with_unsupported_character(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.text(0, 0, "?")
        lcd.triangle.assert_not_called()
        lcd.rect.assert_not_called()

    def test_fontSize(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE)
        self.assertEqual(font16seg.fontSize(), (46, 72))

    def test_fontSize_min(self):
        font16seg.attrib16seg(3, 2, lcd.WHITE)
        self.assertEqual(font16seg.fontSize(), (14, 26))
