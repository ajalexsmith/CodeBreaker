from pixy2.build.python_demos import pixy
from ctypes import *
from pixy import *

def calColour():
    pixy.init ()
    pixy.change_prog ("video");

    X = 158
    Y = 104

    RGB = video_get_RGB (X, Y)
    print(RGB)
    return RGB


