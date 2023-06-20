from imports import *

# Kolizja czyli porownywanie pozycji dwoch obiektow
def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if ((x1 <= x2 <= x1 + w1) or (x2 + w2 >= x1 >= x2)) and ((y1 <= y2 <= y1 + h1) or (y2 + h2 >= y1 >= y2)):
        return True


def out_of_bounds(obj):
    if obj.x < 0 or obj.x > BARS_RIGHT + 8 or obj.y < 0 or obj.y > BARS_BOTTOM + 16:
        return True
