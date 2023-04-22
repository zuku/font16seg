"""
m5stack.lcd mock
"""

"""Color"""
BLACK       = 0x000000
BLUE        = 0x0000ff
CYAN        = 0x00ffff
DARKCYAN    = 0x008080
DARKGREEN   = 0x008000
DARKGREY    = 0x808080
GREEN       = 0x00ff00
GREENYELLOW = 0xacfc2c
LIGHTGREY   = 0xc0c0c0
MAGENTA     = 0xfc00ff
MAROON      = 0x800000
NAVY        = 0x000080
OLIVE       = 0x808000
ORANGE      = 0xfca400
PINK        = 0xfcc0ca
PURPLE      = 0x800080
RED         = 0xfc0000
WHITE       = 0xfcfcfc
YELLOW      = 0xfcfc00

"""Color depth"""
COLOR_BITS16 = 16
COLOR_BITS24 = 24
SPRITE_1BIT  =  1
SPRITE_8BIT  =  8
SPRITE_16BIT = 16

"""Position"""
CENTER = -0x232b
BOTTOM = -0x232c
RIGHT  = -0x232c
LASTX  =  0x1b58
LASTY  =  0x1f40

def screensize():
    return (136, 241)

def get_fg():
    return WHITE

def triangle(x, y, x1, y1, color=None, fillcolor=None):
    pass

def rect(x, y, w, h, color=None, fillcolor=None):
    pass

def circle(x, y, r, color=None, fillcolor=None):
    pass
