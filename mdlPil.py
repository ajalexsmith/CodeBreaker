
from gfxhat import lcd
from PIL import Image, ImageFont, ImageDraw
import mdlIcon


def displaySetup(image):
    draw = ImageDraw.Draw(image)

    draw.rectangle([(0, 5), (127, 5)], 0, 1)

    return image


def creatImage():
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))

    image = displaySetup(image)

    return image

def rotateImage(image, angle):
    image = image.rotate(angle)
    return image

def TB(connencted, image, controller):
    draw = ImageDraw.Draw(image)

    x = 0 + (controller * 20) - 20

    draw.point(mdlIcon.TB(x,0,controller), 1)


    if connencted == True:
        draw.point(mdlIcon.smallTick((12 + x),0), 1)
    else:
        draw.point(mdlIcon.smallCross((12 + x),0), 1)
        
    return image


def Controller(connencted, image):
    draw = ImageDraw.Draw(image)

    draw.point(mdlIcon.smallCont(116,0), 1)

    if connencted == True:
        draw.point(mdlIcon.smallTick(123, 0), 1)
    else:
        draw.point(mdlIcon.smallCross(124,0), 1)
    return image