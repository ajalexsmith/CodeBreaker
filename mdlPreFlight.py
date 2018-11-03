import subprocess as sp
import mdlPil
import mdlGFX


def PreFlight():
    image = mdlPil.creatImage()
    image = ControllerCheck(image)
    mdlGFX.gfxDisplay(image)



def ControllerCheck(draw):
    stdoutdata = sp.getoutput("hcitool con")

    if "00:06:F7:13:66:8F" in stdoutdata.split():
        image = mdlPil.Controller(True, draw)
    else:
        image = mdlPil.Controller(False, draw)

    return image
