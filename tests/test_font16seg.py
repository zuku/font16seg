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

        with self.assertRaises(ValueError):
            font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=1)
        with self.assertRaises(ValueError):
            font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=360)
        with self.assertRaises(ValueError):
            font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=-90)

    def test_attrib16seg_rotate_keep_value(self):
        font16seg.attrib16seg(10, 8, lcd.BLUE, rotate=270)
        self.assertEqual(font16seg._rotate, 270)

        font16seg.attrib16seg(10, 8, lcd.RED)
        self.assertEqual(font16seg._rotate, 270)

    def test_resetAttributes(self):
        font16seg.attrib16seg(10, 8, lcd.BLUE, unlit_color=lcd.RED, letter_spacing=6, rotate=270)
        self.assertEqual(font16seg._length, 10)
        self.assertEqual(font16seg._width, 8)
        self.assertEqual(font16seg._color, lcd.BLUE)
        self.assertEqual(font16seg._unlit_color, lcd.RED)
        self.assertEqual(font16seg._letter_spacing, 6)
        self.assertEqual(font16seg._rotate, 270)

        font16seg.resetAttributes()
        self.assertEqual(font16seg._length, 4)
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

    def test_text_with_colon(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()
        lcd.circle = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.text(0, 0, "0:0")
        self.assertEqual(lcd.triangle.call_count, 40)
        self.assertEqual(lcd.rect.call_count, 16)
        self.assertEqual(lcd.circle.call_count, 2)

    def test_text_with_semi_colon(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()
        lcd.circle = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.text(0, 0, "0;0")
        self.assertEqual(lcd.triangle.call_count, 40)
        self.assertEqual(lcd.rect.call_count, 16)
        lcd.circle.assert_not_called()

    def test_text_with_period(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()
        lcd.circle = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.text(0, 0, "0.0")
        self.assertEqual(lcd.triangle.call_count, 40)
        self.assertEqual(lcd.rect.call_count, 16)
        self.assertEqual(lcd.circle.call_count, 1)

    def test_text_with_comma(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()
        lcd.circle = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.text(0, 0, "0,0")
        self.assertEqual(lcd.triangle.call_count, 40)
        self.assertEqual(lcd.rect.call_count, 16)
        lcd.circle.assert_not_called()

    def test_fontSize(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE)
        self.assertEqual(font16seg.fontSize(), (46, 72))

    def test_fontSize_min(self):
        font16seg.attrib16seg(3, 2, lcd.WHITE)
        self.assertEqual(font16seg.fontSize(), (14, 26))

    def test_textWidth(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=1)
        self.assertEqual(font16seg.textWidth("012345"), 46*6+1*5)

    def test_textWidth_with_0_length_string(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=1)
        self.assertEqual(font16seg.textWidth(""), 0)

    def test_textWidth_with_1_length_string(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=1)
        self.assertEqual(font16seg.textWidth("A"), 46)

    def test_textWidth_with_unsupported_characters(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=2)
        self.assertEqual(font16seg.textWidth("0#!1?@"), 46*6+2*5)

    def test_textWidth_with_colon(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=2)
        self.assertEqual(font16seg.textWidth("00:00"), 46*4+8+2*4)

    def test_textWidth_with_colon_only(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=1)
        self.assertEqual(font16seg.textWidth(":"), 8)

    def test_textWidth_with_period(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=2)
        self.assertEqual(font16seg.textWidth("100.0"), 46*4+8+2*4)

    def test_textWidth_with_period_only(self):
        font16seg.attrib16seg(10, 8, lcd.WHITE, letter_spacing=1)
        self.assertEqual(font16seg.textWidth("."), 8)

    def test_assign(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.assign(ord("d"), 0b0000001111000111)
        font16seg.text(0, 0, "d")
        self.assertEqual(lcd.triangle.call_count, 14)
        self.assertEqual(lcd.rect.call_count, 7)

    def test_assign_min(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.assign(ord("x"), 0)
        font16seg.text(0, 0, "x")
        lcd.triangle.assert_not_called()
        lcd.rect.assert_not_called()

    def test_assign_max(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)
        font16seg.assign(ord("x"), 0b1111111111111111)
        font16seg.text(0, 0, "x")
        self.assertEqual(lcd.triangle.call_count, 32)
        self.assertEqual(lcd.rect.call_count, 12)

    def test_assign_out_of_range(self):
        with self.assertRaises(ValueError):
            font16seg.assign(ord("x"), -1)

        with self.assertRaises(ValueError):
            font16seg.assign(ord("x"), 0b10000000000000000)

    def test_assign_overwrite(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()

        font16seg.attrib16seg(8, 2, lcd.WHITE, unlit_color=None)

        font16seg.text(0, 0, "1")
        self.assertEqual(lcd.triangle.call_count, 4)
        self.assertEqual(lcd.rect.call_count, 2)

        lcd.triangle.reset_mock()
        lcd.rect.reset_mock()

        font16seg.assign(ord("1"), 0b1000100000010011)
        font16seg.text(0, 0, "1")
        self.assertEqual(lcd.triangle.call_count, 10)
        self.assertEqual(lcd.rect.call_count, 5)
