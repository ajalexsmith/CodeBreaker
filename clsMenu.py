import mdlPil, mdlGFX, signal, mdlPreFlight, mdlDrive
from subprocess import call
from gfxhat import touch, lcd, backlight

cur = 0
menuOptions = None

def menuCheck():
    global cur, menuOptions

    if cur < 0 :
        cur = len(menuOptions) - 1
    elif cur == len(menuOptions):
        cur = 0

    return cur


def startBalastOff():
    print("Strt")

def drive():
    mdlDrive.StartMotion()


def startCalibrate():
    RGB = mdlImageProcessing.calColour()
    with open("Resources/colours.txt", "a") as f:
        f.write(str(RGB))

def poweroff():
    mdlGFX.off()
    call("sudo poweroff", shell=True)
def reboot():
    mdlGFX.off()
    call("sudo reboot", shell=True)



def handler(ch, event):
    global menuOptions, cur
    if event == 'press':

        touch.set_led(ch, 1)
        if ch == 3:
            cur += 1
        elif ch == 5:
            cur -= 1

        if ch == 4:
            touch.set_led(ch, 0)
            menuOptions[cur][1]()
        else:
            cur = menuCheck()
        ShowOption(menuOptions[cur])
        touch.set_led(ch, 0)

def addOptions():
    options = []
    options.append([mdlPil.blastOff, startBalastOff])
    options.append([mdlPil.hubble, drive])
    options.append([mdlPil.SpaceInvaders, drive])
    options.append([mdlPil.PiNoon, drive])
    options.append([mdlPil.COM, drive])
    options.append([mdlPil.SOC, drive])
    options.append([mdlPil.drive, drive])
    options.append([mdlPil.calibrate, startCalibrate])
    options.append([mdlPil.settings, drive])
    options.append([mdlPil.poweroff, poweroff])
    options.append([mdlPil.reboot, reboot])
    return options

def ShowOption(MenuOption):
    image = mdlPreFlight.PreFlight()
    image = MenuOption[0](image)
    mdlGFX.gfxDisplay(image)

def Menu():
    global menuOptions, cur
    menuOptions = addOptions()
    ShowOption(menuOptions[cur])

    for x in range(6):
        touch.on(x, handler)

    try:
        signal.pause()
    except KeyboardInterrupt:
        for x in range(6):
            backlight.set_pixel(x, 0, 0, 0)
            touch.set_led(x, 0)
        backlight.show()
        lcd.clear()
        lcd.show()







