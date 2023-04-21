from m5stack import lcd

__TYPE_16SEG = 0

__CHARACTERS = {
    0x20: {'t': __TYPE_16SEG, 'f': 0b0000000000000000},  # [SP]
    0x25: {'t': __TYPE_16SEG, 'f': 0b1010110110110101},  # %
    0x2A: {'t': __TYPE_16SEG, 'f': 0b0001110110111000},  # *
    0x2B: {'t': __TYPE_16SEG, 'f': 0b0000100110010000},  # +
    0x2D: {'t': __TYPE_16SEG, 'f': 0b0000000110000000},  # -
    0x2F: {'t': __TYPE_16SEG, 'f': 0b0000010000100000},  # /
    0x30: {'t': __TYPE_16SEG, 'f': 0b1110011001100111},  # 0
    0x31: {'t': __TYPE_16SEG, 'f': 0b0000100000010000},  # 1
    0x32: {'t': __TYPE_16SEG, 'f': 0b1100001111000011},  # 2
    0x33: {'t': __TYPE_16SEG, 'f': 0b1100001110000111},  # 3
    0x34: {'t': __TYPE_16SEG, 'f': 0b0010001110000100},  # 4
    0x35: {'t': __TYPE_16SEG, 'f': 0b1110000110000111},  # 5
    0x36: {'t': __TYPE_16SEG, 'f': 0b1110000111000111},  # 6
    0x37: {'t': __TYPE_16SEG, 'f': 0b1110001000000100},  # 7
    0x38: {'t': __TYPE_16SEG, 'f': 0b1110001111000111},  # 8
    0x39: {'t': __TYPE_16SEG, 'f': 0b1110001110000111},  # 9
    0x3C: {'t': __TYPE_16SEG, 'f': 0b0000010000001000},  # <
    0x3E: {'t': __TYPE_16SEG, 'f': 0b0001000000100000},  # >
    0x41: {'t': __TYPE_16SEG, 'f': 0b1110001111000100},  # A
    0x42: {'t': __TYPE_16SEG, 'f': 0b1100101010010111},  # B
    0x43: {'t': __TYPE_16SEG, 'f': 0b1110000001000011},  # C
    0x44: {'t': __TYPE_16SEG, 'f': 0b1100101000010111},  # D
    0x45: {'t': __TYPE_16SEG, 'f': 0b1110000111000011},  # E
    0x46: {'t': __TYPE_16SEG, 'f': 0b1110000111000000},  # F
    0x47: {'t': __TYPE_16SEG, 'f': 0b1110000011000111},  # G
    0x48: {'t': __TYPE_16SEG, 'f': 0b0010001111000100},  # H
    0x49: {'t': __TYPE_16SEG, 'f': 0b1100100000010011},  # I
    0x4A: {'t': __TYPE_16SEG, 'f': 0b0000001001000111},  # J
    0x4B: {'t': __TYPE_16SEG, 'f': 0b0010010101001000},  # K
    0x4C: {'t': __TYPE_16SEG, 'f': 0b0010000001000011},  # L
    0x4D: {'t': __TYPE_16SEG, 'f': 0b0011011001000100},  # M
    0x4E: {'t': __TYPE_16SEG, 'f': 0b0011001001001100},  # N
    0x4F: {'t': __TYPE_16SEG, 'f': 0b1110001001000111},  # O
    0x50: {'t': __TYPE_16SEG, 'f': 0b1110001111000000},  # P
    0x51: {'t': __TYPE_16SEG, 'f': 0b1110001001001111},  # Q
    0x52: {'t': __TYPE_16SEG, 'f': 0b1110001111001000},  # R
    0x53: {'t': __TYPE_16SEG, 'f': 0b1101000000001011},  # S
    0x54: {'t': __TYPE_16SEG, 'f': 0b1100100000010000},  # T
    0x55: {'t': __TYPE_16SEG, 'f': 0b0010001001000111},  # U
    0x56: {'t': __TYPE_16SEG, 'f': 0b0010010001100000},  # V
    0x57: {'t': __TYPE_16SEG, 'f': 0b0010001001101100},  # W
    0x58: {'t': __TYPE_16SEG, 'f': 0b0001010000101000},  # X
    0x59: {'t': __TYPE_16SEG, 'f': 0b0001010000010000},  # Y
    0x5A: {'t': __TYPE_16SEG, 'f': 0b1100010000100011},  # Z
    0x5B: {'t': __TYPE_16SEG, 'f': 0b0100100000010001},  # [
    0x5C: {'t': __TYPE_16SEG, 'f': 0b0001000000001000},  # \
    0x5D: {'t': __TYPE_16SEG, 'f': 0b1000100000010010},  # ]
    0x5F: {'t': __TYPE_16SEG, 'f': 0b0000000000000011},  # _
}

__DEFAULT_CHARACTER_CODE = 0x20  # [SP]

_length = 8
_width = 2
_color = lcd.get_fg()
_blank_color = None
_letter_spacing = 3
_rotate = 0

def __horizontal_bar(x, y, l, w, color):
    if color is None:
        return
    hw = round(w / 2)
    lcd.triangle(x+hw, y+hw, x+w, y, x+w, y+w-1, color, color)
    lcd.triangle(x+w+hw+l, y+hw, x+w+l, y, x+w+l, y+w-1, color, color)
    lcd.rect(x+w, y, l, w, color, color)

def __vertical_bar(x, y, l, w, color):
    if color is None:
        return
    hw = round(w / 2)
    lcd.triangle(x+hw, y+hw, x+1, y+w, x+w-1, y+w, color, color)
    lcd.triangle(x+hw, y+w+l+hw, x+1, y+w+l, x+w-1, y+w+l, color, color)
    lcd.rect(x, y+w, w, l, color, color)

def __diagonal_bar(x1, y1, x2, y2, w, color):
    if color is None:
        return
    lcd.triangle(x1, y1, x1, y1+w, x2, y2, color, color)
    lcd.triangle(x2, y2, x2, y2-w, x1, y1, color, color)

def __draw_16seg(x, y, l, w, flags, color, blank_color=None):
    __horizontal_bar(x, y, l, w,                                        color if flags & 0b1000000000000000 > 0 else blank_color)
    __horizontal_bar(x+w+l+1, y, l, w,                                  color if flags & 0b0100000000000000 > 0 else blank_color)
    __vertical_bar(x, y+2, l*2, w,                                      color if flags & 0b0010000000000000 > 0 else blank_color)
    __diagonal_bar(x+w+1, y+w+1, x+w+l, y+w+4+l*2, w,                   color if flags & 0b0001000000000000 > 0 else blank_color)
    __vertical_bar(x+w+l+1, y+2, l*2, w,                                color if flags & 0b0000100000000000 > 0 else blank_color)
    __diagonal_bar(x+w*2+l*2+1, y+w+1, x+w*2+l+2, y+w+4+l*2, w,         color if flags & 0b0000010000000000 > 0 else blank_color)
    __vertical_bar(x+w*2+l*2+2, y+2, l*2, w,                            color if flags & 0b0000001000000000 > 0 else blank_color)
    __horizontal_bar(x, y+w+4+l*2, l, w,                                color if flags & 0b0000000100000000 > 0 else blank_color)
    __horizontal_bar(x+w+l+1, y+w+4+l*2, l, w,                          color if flags & 0b0000000010000000 > 0 else blank_color)
    __vertical_bar(x, y+w+7+l*2, l*2, w,                                color if flags & 0b0000000001000000 > 0 else blank_color)
    __diagonal_bar(x+w+l, y+w*2+5+l*2, x+w+1, y+w*2+7+l*4, w,           color if flags & 0b0000000000100000 > 0 else blank_color)
    __vertical_bar(x+w+l+1, y+w+7+l*2, l*2, w,                          color if flags & 0b0000000000010000 > 0 else blank_color)
    __diagonal_bar(x+w*2+l+2, y+w*2+5+l*2, x+w*2+l*2+1, y+w*2+7+l*4, w, color if flags & 0b0000000000001000 > 0 else blank_color)
    __vertical_bar(x+w*2+3+l*2, y+w+7+l*2, l*2, w,                      color if flags & 0b0000000000000100 > 0 else blank_color)
    __horizontal_bar(x, y+w*2+8+l*4, l, w,                              color if flags & 0b0000000000000010 > 0 else blank_color)
    __horizontal_bar(x+w+l+1, y+w*2+8+l*4, l, w,                        color if flags & 0b0000000000000001 > 0 else blank_color)

def __calc_16seg_character_width(l, w):
    return l * 2 + w * 3 + 2

def fontSize():
    # TODO
    pass

def textWidth(txt):
    # TODO
    pass

def attrib16seg(length, width, color, *, blank_color=-1, letter_spacing=None, rotate=0):
    """
    Set attributes of the 16-segment font.

    Parameters
    ----------
    length : int
        Segment length.
        Length of a rectangular part of a short (horizontal) segment.
    width : int
        Segment width.
    color : int
        Text color.
    blank_color : int
        Color of unlit segments.
    letter_spacing : int
        Distance between characters.
    rotate : int
        Font rotation angle.
        Only accepts 0, 90, 180 and 270.
    """
    global _length, _width, _color, _blank_color, _letter_spacing, _rotate

    if length < 3:
        length = 3
    if width < 2:
        width = 2
    if width > length:
        width = length

    _length = length
    _width = width
    _color = color
    if blank_color != -1:
        _blank_color = blank_color
    if letter_spacing is not None:
        if letter_spacing < 0:
            letter_spacing = 0
        _letter_spacing = letter_spacing
    if rotate in (0, 90, 180, 270):  # TODO
        _rotate = rotate

def text(x, y, txt, *, color=None, blank_color=None):
    """
    Display the string txt as 16-segment at position (x, y).

    Paramters
    ---------
    x : int
        Horizontal position of the top left of the text.
    y : int
        Vertical position of the top left of the text.
    txt : str
        String to display.
        Only supported characters are displayed. Other characters are displayed as spaces.
    color : int
        Text color.
    blank_color : int
        Color of unlit segments.
    """
    if color is None:
        color = _color
    if blank_color is None:
        blank_color = _blank_color

    for c in txt:
        character = __CHARACTERS.get(ord(c), __CHARACTERS[__DEFAULT_CHARACTER_CODE])
        __draw_16seg(x, y, _length, _width, character['f'], color, blank_color)
        x += __calc_16seg_character_width(_length, _width) + _letter_spacing
