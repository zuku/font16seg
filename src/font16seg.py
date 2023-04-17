from m5stack import lcd

def __draw_horizon(x, y, l, w, color):
    if color is None:
        return
    hw = round(w / 2)
    lcd.triangle(x+hw, y+hw, x+w, y, x+w, y+w-1, color, color)
    lcd.triangle(x+w+hw+l, y+hw, x+w+l, y, x+w+l, y+w-1, color, color)
    lcd.rect(x+w, y, l, w, color, color)

def __draw_vertical(x, y, l, w, color):
    if color is None:
        return
    hw = round(w / 2)
    lcd.triangle(x+hw, y+hw, x+1, y+w, x+w-1, y+w, color, color)
    lcd.triangle(x+hw, y+w+l+hw, x+1, y+w+l, x+w-1, y+w+l, color, color)
    lcd.rect(x, y+w, w, l, color, color)

def __draw_diagonal(x1, y1, x2, y2, w, color):
    if color is None:
        return
    lcd.triangle(x1, y1, x1, y1+w, x2, y2, color, color)
    lcd.triangle(x2, y2, x2, y2-w, x1, y1, color, color)

def __draw_16seg(x, y, l, w, flags, color, blank_color=None):
    __draw_horizon(x, y, l, w, color if flags & 0b1000000000000000 > 0 else blank_color)
    __draw_horizon(x+w+l+1, y, l, w, color if flags & 0b0100000000000000 > 0 else blank_color)
    __draw_vertical(x, y+2, l*2, w, color if flags & 0b0010000000000000 > 0 else blank_color)
    __draw_diagonal(x+w+1, y+w+1, x+w+l, y+w+4+l*2, w, color if flags & 0b0001000000000000 > 0 else blank_color)
    __draw_vertical(x+w+l+1, y+2, l*2, w, color if flags & 0b000010000000000 > 0 else blank_color)
    __draw_diagonal(x+w*2+l*2+1, y+w+1, x+w*2+l+2, y+w+4+l*2, w, color if flags & 0b0000010000000000 > 0 else blank_color)
    __draw_vertical(x+w*2+l*2+2, y+2, l*2, w, color if flags & 0b0000001000000000 > 0 else blank_color)
    __draw_horizon(x, y+w+4+l*2, l, w, color if flags & 0b0000000100000000 > 0 else blank_color)
    __draw_horizon(x+w+l+1, y+w+4+l*2, l, w, color if flags & 0b0000000010000000 > 0 else blank_color)
    __draw_vertical(x, y+w+7+l*2, l*2, w, color if flags & 0b0000000001000000 > 0 else blank_color)
    __draw_diagonal(x+w+l, y+w*2+5+l*2, x+w+1, y+w*2+7+l*4, w, color if flags & 0b0000000000100000 > 0 else blank_color)
    __draw_vertical(x+w+l+1, y+w+7+l*2, l*2, w, color if flags & 0b0000000000010000 > 0 else blank_color)
    __draw_diagonal(x+w*2+l+2, y+w*2+5+l*2, x+w*2+l*2+1, y+w*2+7+l*4, w, color if flags & 0b0000000000001000 > 0 else blank_color)
    __draw_vertical(x+w*2+3+l*2, y+w+7+l*2, l*2, w, color if flags & 0b0000000000000100 > 0 else blank_color)
    __draw_horizon(x, y+w*2+8+l*4, l, w, color if flags & 0b0000000000000010 > 0 else blank_color)
    __draw_horizon(x+w+l+1, y+w*2+8+l*4, l, w, color if flags & 0b0000000000000001 > 0 else blank_color)
