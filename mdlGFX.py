
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


def gfxDisplay(image):
    for x in range(128):
        for y in range(64):
            pixel = image.getpixel((x, y))
            lcd.set_pixel(x, y, pixel)
    lcd.show()

def GFXbacklight(r, g, b):
    for x in range(6):
        backlight.set_pixel(x, r, g, b)
    backlight.show()