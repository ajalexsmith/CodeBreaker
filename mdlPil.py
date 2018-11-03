
from gfxhat import lcd
from PIL import Image, ImageFont, ImageDraw

def displaySetup(image):
    draw = ImageDraw.Draw(image)

    draw.rectangle([(0, 5), (127, 5)], 0, 1)

    return image


def creatImage():
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))

    image = displaySetup(image)

    return image



def Controller(connencted, image):
    draw = ImageDraw.Draw(image)

    draw.point([(121, 1),(121, 2),(121, 3),(120, 0),(120, 2),(119, 1),(118, 1),(117, 0),(117, 2),(116, 1),(116, 2),(116, 3),], 1)

    if connencted == True:
       draw.point([(127,0),(126,1),(125,2),(124,3),(123,2)] ,1)
    else:
        draw.point([(127, 0),(127, 3),(126, 1),(126, 2),(125, 1),(125, 2),(124, 0),(124, 3)], 1)
    return image