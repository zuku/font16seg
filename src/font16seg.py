from m5stack import lcd

__TYPE_16SEG = 0

__CHARACTERS = {
    0x20: (__TYPE_16SEG, 0b0000000000000000),  # [SP]
    0x25: (__TYPE_16SEG, 0b1010110110110101),  # %
    0x2A: (__TYPE_16SEG, 0b0001110110111000),  # *
    0x2B: (__TYPE_16SEG, 0b0000100110010000),  # +
    0x2D: (__TYPE_16SEG, 0b0000000110000000),  # -
    0x2F: (__TYPE_16SEG, 0b0000010000100000),  # /
    0x30: (__TYPE_16SEG, 0b1110011001100111),  # 0
    0x31: (__TYPE_16SEG, 0b0000100000010000),  # 1
    0x32: (__TYPE_16SEG, 0b1100001111000011),  # 2
    0x33: (__TYPE_16SEG, 0b1100001110000111),  # 3
    0x34: (__TYPE_16SEG, 0b0010001110000100),  # 4
    0x35: (__TYPE_16SEG, 0b1110000110000111),  # 5
    0x36: (__TYPE_16SEG, 0b1110000111000111),  # 6
    0x37: (__TYPE_16SEG, 0b1110001000000100),  # 7
    0x38: (__TYPE_16SEG, 0b1110001111000111),  # 8
    0x39: (__TYPE_16SEG, 0b1110001110000111),  # 9
    0x3C: (__TYPE_16SEG, 0b0000010000001000),  # <
    0x3E: (__TYPE_16SEG, 0b0001000000100000),  # >
    0x41: (__TYPE_16SEG, 0b1110001111000100),  # A
    0x42: (__TYPE_16SEG, 0b1100101010010111),  # B
    0x43: (__TYPE_16SEG, 0b1110000001000011),  # C
    0x44: (__TYPE_16SEG, 0b1100101000010111),  # D
    0x45: (__TYPE_16SEG, 0b1110000111000011),  # E
    0x46: (__TYPE_16SEG, 0b1110000111000000),  # F
    0x47: (__TYPE_16SEG, 0b1110000011000111),  # G
    0x48: (__TYPE_16SEG, 0b0010001111000100),  # H
    0x49: (__TYPE_16SEG, 0b1100100000010011),  # I
    0x4A: (__TYPE_16SEG, 0b0000001001000111),  # J
    0x4B: (__TYPE_16SEG, 0b0010010101001000),  # K
    0x4C: (__TYPE_16SEG, 0b0010000001000011),  # L
    0x4D: (__TYPE_16SEG, 0b0011011001000100),  # M
    0x4E: (__TYPE_16SEG, 0b0011001001001100),  # N
    0x4F: (__TYPE_16SEG, 0b1110001001000111),  # O
    0x50: (__TYPE_16SEG, 0b1110001111000000),  # P
    0x51: (__TYPE_16SEG, 0b1110001001001111),  # Q
    0x52: (__TYPE_16SEG, 0b1110001111001000),  # R
    0x53: (__TYPE_16SEG, 0b1101000000001011),  # S
    0x54: (__TYPE_16SEG, 0b1100100000010000),  # T
    0x55: (__TYPE_16SEG, 0b0010001001000111),  # U
    0x56: (__TYPE_16SEG, 0b0010010001100000),  # V
    0x57: (__TYPE_16SEG, 0b0010001001101100),  # W
    0x58: (__TYPE_16SEG, 0b0001010000101000),  # X
    0x59: (__TYPE_16SEG, 0b0001010000010000),  # Y
    0x5A: (__TYPE_16SEG, 0b1100010000100011),  # Z
    0x5B: (__TYPE_16SEG, 0b0100100000010001),  # [
    0x5C: (__TYPE_16SEG, 0b0001000000001000),  # \
    0x5D: (__TYPE_16SEG, 0b1000100000010010),  # ]
    0x5F: (__TYPE_16SEG, 0b0000000000000011),  # _
}

__DEFAULT_CHARACTER_CODE = 0x20  # [SP]

_length = None
_width = None
_color = None
_unlit_color = None
_letter_spacing = None
_rotate = None

def resetAttributes():
    """
    Reset attributes.
    """
    global _length, _width, _color, _unlit_color, _letter_spacing, _rotate
    _length = 4
    _width = 2
    _color = lcd.get_fg()
    _unlit_color = None
    _letter_spacing = 3
    _rotate = 0

resetAttributes()

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

def __diagonal_bar_v(x1, y1, x2, y2, w, color):
    if color is None:
        return
    lcd.triangle(x1, y1, x1, y1+w, x2, y2, color, color)
    lcd.triangle(x2, y2, x2, y2-w, x1, y1, color, color)

def __diagonal_bar_h(x1, y1, x2, y2, w, color):
    if color is None:
        return
    lcd.triangle(x1, y1, x1-w, y1, x2, y2, color, color)
    lcd.triangle(x2, y2, x2+w, y2, x1, y1, color, color)

def __color(color, unlit_color, flags, segment):
    if flags & (1 << (16 - segment)) > 0:
        return color
    return unlit_color

def __draw_16seg(x, y, l, w, flags, color, unlit_color=None):
    if _rotate == 0:
        __horizontal_bar(x, y, l, w,                                          __color(color, unlit_color, flags, 1))
        __horizontal_bar(x+w+l+1, y, l, w,                                    __color(color, unlit_color, flags, 2))
        __vertical_bar(x, y+2, l*2, w,                                        __color(color, unlit_color, flags, 3))
        __diagonal_bar_v(x+w+1, y+w+1, x+w+l, y+w+l*2+4, w,                   __color(color, unlit_color, flags, 4))
        __vertical_bar(x+w+l+1, y+2, l*2, w,                                  __color(color, unlit_color, flags, 5))
        __diagonal_bar_v(x+w*2+l*2+1, y+w+1, x+w*2+l+2, y+w+l*2+4, w,         __color(color, unlit_color, flags, 6))
        __vertical_bar(x+w*2+l*2+2, y+2, l*2, w,                              __color(color, unlit_color, flags, 7))
        __horizontal_bar(x, y+w+l*2+4, l, w,                                  __color(color, unlit_color, flags, 8))
        __horizontal_bar(x+w+l+1, y+w+l*2+4, l, w,                            __color(color, unlit_color, flags, 9))
        __vertical_bar(x, y+w+l*2+7, l*2, w,                                  __color(color, unlit_color, flags, 10))
        __diagonal_bar_v(x+w+l, y+w*2+l*2+5, x+w+1, y+w*2+l*4+7, w,           __color(color, unlit_color, flags, 11))
        __vertical_bar(x+w+l+1, y+w+l*2+7, l*2, w,                            __color(color, unlit_color, flags, 12))
        __diagonal_bar_v(x+w*2+l+2, y+w*2+l*2+5, x+w*2+l*2+1, y+w*2+l*4+7, w, __color(color, unlit_color, flags, 13))
        __vertical_bar(x+w*2+l*2+3, y+w+l*2+7, l*2, w,                        __color(color, unlit_color, flags, 14))
        __horizontal_bar(x, y+w*2+l*4+8, l, w,                                __color(color, unlit_color, flags, 15))
        __horizontal_bar(x+w+l+1, y+w*2+l*4+8, l, w,                          __color(color, unlit_color, flags, 16))
    elif _rotate == 90:
        __vertical_bar(x-w, y, l, w,                                          __color(color, unlit_color, flags, 1))
        __vertical_bar(x-w, y+w+l+1, l, w,                                    __color(color, unlit_color, flags, 2))
        __horizontal_bar(x-w*2-l*2-2, y, l*2, w,                              __color(color, unlit_color, flags, 3))
        __diagonal_bar_h(x-w-1, y+w+1, x-w-l*2-4, y+w+l, w,                   __color(color, unlit_color, flags, 4))
        __horizontal_bar(x-w*2-l*2-2, y+w+l+1, l*2, w,                        __color(color, unlit_color, flags, 5))
        __diagonal_bar_h(x-w-1, y+w*2+l*2+1, x-w-l*2-4, y+w*2+l+2, w,         __color(color, unlit_color, flags, 6))
        __horizontal_bar(x-w*2-l*2-2, y+w*2+l*2+2, l*2, w,                    __color(color, unlit_color, flags, 7))
        __vertical_bar(x-w*2-l*2-4, y, l, w,                                  __color(color, unlit_color, flags, 8))
        __vertical_bar(x-w*2-l*2-4, y+w+l+1, l, w,                            __color(color, unlit_color, flags, 9))
        __horizontal_bar(x-w*3-l*4-6, y, l*2, w,                              __color(color, unlit_color, flags, 10))
        __diagonal_bar_h(x-w*2-l*2-5, y+w+l, x-w*2-l*4-5, y+w+1, w,           __color(color, unlit_color, flags, 11))
        __horizontal_bar(x-w*3-l*4-6, y+w+l+1, l*2, w,                        __color(color, unlit_color, flags, 12))
        __diagonal_bar_h(x-w*2-l*2-5, y+w*2+l+2, x-w*2-l*4-5, y+w*2+l*2+1, w, __color(color, unlit_color, flags, 13))
        __horizontal_bar(x-w*3-l*4-6, y+w*2+l*2+2, l*2, w,                    __color(color, unlit_color, flags, 14))
        __vertical_bar(x-w*3-l*4-8, y, l, w,                                  __color(color, unlit_color, flags, 15))
        __vertical_bar(x-w*3-l*4-8, y+w+l+1, l, w,                            __color(color, unlit_color, flags, 16))
    elif _rotate == 180:
        __horizontal_bar(x-w*2-l, y-w, l, w,                                  __color(color, unlit_color, flags, 1))
        __horizontal_bar(x-w*3-l*2-2, y-w, l, w,                              __color(color, unlit_color, flags, 2))
        __vertical_bar(x-w, y-w*2-l*2-2, l*2, w,                              __color(color, unlit_color, flags, 3))
        __diagonal_bar_v(x-w-l, y-w-l*2-3, x-w-1, y-w-1, w,                   __color(color, unlit_color, flags, 4))
        __vertical_bar(x-w*2-l-1, y-w*2-l*2-2, l*2, w,                        __color(color, unlit_color, flags, 5))
        __diagonal_bar_v(x-w*2-l-2, y-w-l*2-3, x-w*2-l*2-1, y-w-1, w,         __color(color, unlit_color, flags, 6))
        __vertical_bar(x-w*3-l*2-2, y-w*2-l*2-2, l*2, w,                      __color(color, unlit_color, flags, 7))
        __horizontal_bar(x-w*2-l, y-w*2-l*2-4, l, w,                          __color(color, unlit_color, flags, 8))
        __horizontal_bar(x-w*3-l*2-2, y-w*2-l*2-4, l, w,                      __color(color, unlit_color, flags, 9))
        __vertical_bar(x-w, y-w*3-l*4-6, l*2, w,                              __color(color, unlit_color, flags, 10))
        __diagonal_bar_v(x-w-1, y-w*2-l*4-7, x-w-l, y-w*2-l*2-5, w,           __color(color, unlit_color, flags, 11))
        __vertical_bar(x-w*2-l-1, y-w*3-l*4-6, l*2, w,                        __color(color, unlit_color, flags, 12))
        __diagonal_bar_v(x-w*2-l*2-1, y-w*2-l*4-7, x-w*2-l-2, y-w*2-l*2-5, w, __color(color, unlit_color, flags, 13))
        __vertical_bar(x-w*3-l*2-2, y-w*3-l*4-6, l*2, w,                      __color(color, unlit_color, flags, 14))
        __horizontal_bar(x-w*2-l, y-w*3-l*4-8, l, w,                          __color(color, unlit_color, flags, 15))
        __horizontal_bar(x-w*3-l*2-2, y-w*3-l*4-8, l, w,                      __color(color, unlit_color, flags, 16))
    elif _rotate == 270:
        __vertical_bar(x, y-w*2-l, l, w,                                      __color(color, unlit_color, flags, 1))
        __vertical_bar(x, y-w*3-l*2-2, l, w,                                  __color(color, unlit_color, flags, 2))
        __horizontal_bar(x+2, y-w, l*2, w,                                    __color(color, unlit_color, flags, 3))
        __diagonal_bar_h(x+w+l*2+3, y-w-l, x+w+1, y-w-1, w,                   __color(color, unlit_color, flags, 4))
        __horizontal_bar(x+2, y-w*2-l-1, l*2, w,                              __color(color, unlit_color, flags, 5))
        __diagonal_bar_h(x+w+l*2+3, y-w*2-l-2, x+w+1, y-w*2-l*2-1, w,         __color(color, unlit_color, flags, 6))
        __horizontal_bar(x+2, y-w*3-l*2-2, l*2, w,                            __color(color, unlit_color, flags, 7))
        __vertical_bar(x+w+l*2+4, y-w*2-l, l, w,                              __color(color, unlit_color, flags, 8))
        __vertical_bar(x+w+l*2+4, y-w*3-l*2-2, l, w,                          __color(color, unlit_color, flags, 9))
        __horizontal_bar(x+w+l*2+6, y-w, l*2, w,                              __color(color, unlit_color, flags, 10))
        __diagonal_bar_h(x+w*2+l*4+7, y-w-1, x+w*2+l*2+5, y-w-l, w,           __color(color, unlit_color, flags, 11))
        __horizontal_bar(x+w+l*2+6, y-w*2-l-1, l*2, w,                        __color(color, unlit_color, flags, 12))
        __diagonal_bar_h(x+w*2+l*4+7, y-w*2-l*2-1, x+w*2+l*2+5, y-w*2-l-2, w, __color(color, unlit_color, flags, 13))
        __horizontal_bar(x+w+l*2+6, y-w*3-l*2-2, l*2, w,                      __color(color, unlit_color, flags, 14))
        __vertical_bar(x+w*2+l*4+8, y-w*2-l, l, w,                            __color(color, unlit_color, flags, 15))
        __vertical_bar(x+w*2+l*4+8, y-w*3-l*2-2, l, w,                        __color(color, unlit_color, flags, 16))

def __calc_16seg_character_width(l, w):
    return l * 2 + w * 3 + 2

def __calc_16seg_character_height(l, w):
    return l * 4 + w * 3 + 8

def fontSize():
    """
    Return font size.

    Returns
    -------
    tuple : (width : int, height : int)
        Nominal font sizes.
        (width, height)
    """
    return (__calc_16seg_character_width(_length, _width), __calc_16seg_character_height(_length, _width))

def textWidth(txt):
    """
    Return the width of the string txt.

    Parameters
    ----------
    txt : str
        String to calculate the width.

    Returns
    -------
    int
        The width of the given string.
    """
    width = 0
    text_length = len(txt)
    width += __calc_16seg_character_width(_length, _width) * text_length
    if text_length > 0:
        width += _letter_spacing * (text_length - 1)
    return width

def attrib16seg(length, width, color, *, unlit_color=-1, letter_spacing=None, rotate=None):
    """
    Set attributes of the 16-segment font.

    Parameters
    ----------
    length : int
        Segment length.
        Length of a rectangular part of a short (horizontal) segment.
        Minimum value is 3.
    width : int
        Segment width.
        Minimum value is 2.
    color : int
        Text color.
    unlit_color : int
        Color of unlit segments.
    letter_spacing : int
        Distance between characters.
    rotate : int
        Font rotation angle.
        Only accepts 0, 90, 180 or 270.
    """
    global _length, _width, _color, _unlit_color, _letter_spacing, _rotate

    if length < 3:
        length = 3
    if width < 2:
        width = 2
    if width > length:
        width = length

    _length = length
    _width = width
    _color = color
    if unlit_color != -1:
        _unlit_color = unlit_color
    if letter_spacing is not None:
        if letter_spacing < 0:
            letter_spacing = 0
        _letter_spacing = letter_spacing
    if rotate is not None:
        if rotate in (0, 90, 180, 270):
            _rotate = rotate
        else:
            raise ValueError("rotate parameter only accepts 0, 90, 180 or 270")

def text(x, y, txt, *, color=None, unlit_color=None):
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
    unlit_color : int
        Color of unlit segments.
    """
    if color is None:
        color = _color
    if unlit_color is None:
        unlit_color = _unlit_color

    for c in txt:
        character = __CHARACTERS.get(ord(c), __CHARACTERS[__DEFAULT_CHARACTER_CODE])
        __draw_16seg(x, y, _length, _width, character[1], color, unlit_color)
        delta = __calc_16seg_character_width(_length, _width) + _letter_spacing
        if _rotate == 0:
            x += delta
        elif _rotate == 90:
            y += delta
        elif _rotate == 180:
            x -= delta
        elif _rotate == 270:
            y -= delta
