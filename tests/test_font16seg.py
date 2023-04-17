import unittest
from unittest.mock import MagicMock, call
from m5stack import lcd
import font16seg

class TestFont16seg(unittest.TestCase):
    def test_sample(self):
        lcd.screensize = MagicMock(return_value=(136, 241))
        lcd.triangle = MagicMock()
        lcd.rect = MagicMock()
