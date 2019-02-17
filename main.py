'''

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

 This is the main python file for my PiWars
   Robot. This will call all the functions
   that are required from other files, but
 no code should be written in this document

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


'''

import mdlPreFlight, mdlGFX, clsMenu, clsSettings

_ = clsSettings.globSettings
mdlGFX.GFXbacklight(int(_.blR),int(_.blG), int(_.blB))

try:
    clsMenu.Menu()
except KeyboardInterrupt:
    mdlGFX.off()
