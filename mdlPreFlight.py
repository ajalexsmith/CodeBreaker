import subprocess as sp
import mdlPil, mdlGFX, ThunderBorg


def PreFlight():
    image = mdlPil.creatImage()
    image = ControllerCheck(image)
    image = TBCheck(image)
    mdlGFX.gfxDisplay(image)



def ControllerCheck(image):
    stdoutdata = sp.getoutput("hcitool con")

    if "00:06:F7:13:66:8F" in stdoutdata.split():
        image = mdlPil.Controller(True, image)
    else:
        image = mdlPil.Controller(False, image)

    return image

def TBCheck(image):
    TB1 = ThunderBorg.ThunderBorg()
    TB1.i2cAddress = 10
    TB1.Init()
    image = mdlPil.TB(TB1.foundChip, image, 1)

    TB2 = ThunderBorg.ThunderBorg()
    TB2.i2cAddress = 11
    TB2.Init()
    image = mdlPil.TB(TB1.foundChip, image, 2)
    return image
